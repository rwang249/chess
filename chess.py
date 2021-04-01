#!/usr/bin/env python3

#use inheritance(i.e. board should refer to pieces, and pieces should refer to specific piece's common method(movement))
#use abstraction
#create method to check status of gameboard
#create class to for board
#create class for pieces
#base class of piece
#derivative will be individual pieces
#chess board composition of piece?
import os
import re
import itertools
from piece  import Piece
from bishop import Bishop
from king   import King
from knight import Knight
from pawn   import Pawn
from queen  import Queen
from rook   import Rook

class Chess_Board():
    def __init__(self, pieces):
        self.pieces = pieces
        board = []
        for row in range(8):
            column = []
            board.append(column)
            for columnNum in range(8):
                column.append('  ')
        
        for piece in pieces:
            index = pieces.index(piece)
            pieceLocation = pieces[index].location
            board[pieceLocation[1]][pieceLocation[0]] = str(pieces[index].displayValue).format()
        self.board = board

    def updateBoard(self, pieces):
        self.pieces = pieces
        board = []
        for row in range(8):
            column = []
            board.append(column)
            for columnNum in range(8):
                column.append('  ')
        
        for piece in pieces:
            index = pieces.index(piece)
            pieceLocation = pieces[index].location
            board[pieceLocation[1]][pieceLocation[0]] = str(pieces[index].displayValue).format()
        self.board = board

    def displayBoard(self, board):
        rowNum = 8
        print("  ", end="")
        for row in board:
            print("-" * 41)
            print(str(rowNum), end=" ")
            rowNum -= 1
            for column in row:
                print("| {} ".format(column), end="")
            print("|")
            print("  ", end="")
        print("-" * 41)
        for letter in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            print("   {} ".format(letter), end="")
        print("\n")

    def collisionChecker(self, pieces, sourcePiece, destination, check, player):
        ### need to step flags where once check is achieved don't change. only exit once all pieces have been checked for check
        #calculate displacement
        displacement = []
        isCheck = None

        if check == True:
            for piece in pieces:
                index = pieces.index(piece)
                if player.side != piece.side and (piece.displayValue == "wk" or piece.displayValue == "bk"):
                    kingLocation = pieces[index].location
                    king = piece
                    displacement.append(int(kingLocation[0]) - int(sourcePiece.location[0]))
                    displacement.append(int(kingLocation[1]) - int(sourcePiece.location[1]))
        else:
            displacement.append(int(destination[0]) - int(sourcePiece.location[0]))
            displacement.append(int(destination[1]) - int(sourcePiece.location[1]))           

        if sourcePiece.perpendicular == True and sourcePiece.diagonal == True:
            #specifically for queen
            #east
            if displacement[0] > 0 and displacement[1] == 0:
                orthogonal = [1,0]
            #west
            elif displacement[0] < 0 and displacement[1] == 0:
                orthogonal = [-1,0]
            #north
            elif displacement[1] < 0 and displacement[0] == 0:
                orthogonal = [0,-1]
            #south
            elif displacement[1] > 0 and displacement[0] == 0:
                orthogonal = [0,1]
            else:
                orthogonal = ""

            #northeast
            if displacement[0] > 0 and displacement[1] < 0:
                diagonal = [(1,-1)]
            #northwest
            elif displacement[0] < 0 and displacement[1] < 0:
                diagonal = [(-1,-1)]
            #southeast
            elif displacement[0] > 0 and displacement[1] > 0:
                diagonal = [(1,1)]
            #southwest
            elif displacement[0] < 0 and displacement[1] > 0:
                diagonal = [(-1,1)]
            else:
                diagonal = ""

            try:
                if diagonal != "":
                    for x, y in diagonal:
                        for step in (range(1, abs(int(displacement[0] + 1)))):
                            for piece in pieces:
                                if (int(piece.location[0]) == int(sourcePiece.location[0] + (x * step)) and int(piece.location[1]) == int(sourcePiece.location[1] + (y * step))):
                                    if check == True and sourcePiece.side != piece.side: 
                                        if piece.displayValue == "wk" or piece.displayValue == "bk":
                                            return "check"
                                        else:
                                            return False
                                    elif sourcePiece != piece and sourcePiece.side == piece.side:
                                        return True
                #x Axis
                if displacement[0] != 0 and orthogonal != "":
                    for step in (range(abs(int(displacement[0] + 1)))):
                        print("x: ", str(sourcePiece.location[0] + (x * int(step))))
                        print("y: ",str(sourcePiece.location[1] + (y * int(step))))
                        for piece in pieces:
                            if int(sourcePiece.location[1]) == int(piece.location[1]) and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) == int(piece.location[0]):
                                if check == True and sourcePiece.side != piece.side: 
                                    if piece.displayValue == "wk" or piece.displayValue == "bk":
                                        return "check"
                                    else:
                                        return False
                                elif sourcePiece != piece and sourcePiece.side == piece.side:
                                    return True
                            
                #y Axis
                elif displacement[1] != 0 and orthogonal != "":
                    for step in (range(1, abs(int(displacement[1])))):
                        print("x: ", str(sourcePiece.location[0] + (x * int(step))))
                        print("y: ",str(sourcePiece.location[1] + (y * int(step))))
                        for piece in pieces:
                            if int(sourcePiece.location[0]) == int(piece.location[0]) and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) == int(piece.location[1]):
                                if check == True and sourcePiece.side != piece.side: 
                                    if piece.displayValue == "wk" or piece.displayValue == "bk":
                                        return "check"
                                    else:
                                        return False
                                elif sourcePiece != piece and sourcePiece.side == piece.side:
                                    return True
            except:
                return -1

        elif sourcePiece.perpendicular == True and sourcePiece.diagonal == False:       
            #east
            if displacement[0] > 0 and displacement[1] == 0:
                orthogonal = [1,0]
            #west
            elif displacement[0] < 0 and displacement[1] == 0:
                orthogonal = [-1,0]
            #north
            elif displacement[1] < 0 and displacement[0] == 0:
                orthogonal = [0,-1]
            #south
            elif displacement[1] > 0 and displacement[0] == 0:
                orthogonal = [0,1]
            else:
                orthogonal = ""

            #print("displacement: ", displacement)
            #need to change displacement as for check it will look at ALL pieces towards king, which will always hit when applying displacement
            #pawns are hitting x-axis for some reason
            #x Axis
            if displacement[0] != 0 and orthogonal != "":
                for step in (range(1, abs(int(displacement[0])))):
                    print("x: ", str(int(sourcePiece.location[0] + (int(orthogonal[0]) * step))))
                    #print("y: ", str(int(sourcePiece.location[1] + (int(orthogonal[1]) * step))))
                    for piece in pieces:
                        if int(sourcePiece.location[1]) == int(piece.location[1]) and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) == int(piece.location[0]) \
                        and ((int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) <= piece.distance):
                            if check == True and sourcePiece.side != piece.side: 
                                print("checking check!")
                                if piece.displayValue == "wk" or piece.displayValue == "bk":
                                    return "check"
                                else:
                                    return False
                            elif sourcePiece != piece and sourcePiece.side == piece.side:
                                return True

            ##################not calculating check for rooks. figure out why. might need to play around and see which conditions are getting hit
            # not fully going through pieces array before returning        
            # main things i should store are if i hit check or True. do not change flag once set until returned.
            # why the hell is  <pawn.Pawn object at 0x7f8ad13cf130> being selected as source piece when it is actually rook? is it because of parser?
            # only reporting sourcepiece incorrectly in here
            # issue is that array is not updated immediately after taking a piece. after taking BP source piece is still c, 7
            #y Axis
            elif displacement[1] != 0 and orthogonal != "":
                for step in (range(1, abs(int(displacement[1])))):
                    # print("x: ", str(int(sourcePiece.location[0] + (int(orthogonal[0]) * step))))
                    print("y: ", str(int(sourcePiece.location[1] + (int(orthogonal[1]) * step))))
                    for piece in pieces:
                        if int(sourcePiece.location[0]) == int(piece.location[0]) and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) == int(piece.location[1]) \
                        and ((int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) <= piece.distance):
                            print(sourcePiece)
                            #just for getting rook output
                            print("piece travel distance: ", piece.distance)
                            print("king location:",kingLocation)
                            print("source piece location",sourcePiece.location)
                            print("source piece: ",sourcePiece.displayValue)
                            print("displacement", displacement)
                            print("orthogonal", orthogonal)
                            if sourcePiece.displayValue == "wr" or sourcePiece.displayValue == "br": #delete this line when done testing
                                if check == True:
                                #     print("king location:",kingLocation)
                                #     print("source piece location",sourcePiece.location)
                                #     print("source piece: ",sourcePiece.displayValue)
                                #     print("displacement", displacement)
                                #     print("orthogonal", orthogonal)
                                    print("shit this one")
                                if check == True and sourcePiece.side != piece.side: 
                                    if piece.displayValue == "wk" or piece.displayValue == "bk":
                                        return "check"
                                    else:
                                        return False
                                elif sourcePiece != piece and sourcePiece.side == piece.side:
                                    return True

        elif sourcePiece.diagonal == True and sourcePiece.perpendicular == False:
            #northeast
            if displacement[0] > 0 and displacement[1] < 0:
                diagonal = [(1,-1)]
            #northwest
            elif displacement[0] < 0 and displacement[1] < 0:
                diagonal = [(-1,-1)]
            #southeast
            elif displacement[0] > 0 and displacement[1] > 0:
                diagonal = [(1,1)]
            #southwest
            elif displacement[0] < 0 and displacement[1] > 0:
                diagonal = [(-1,1)]
            else:
                diagonal = ""
            
            # if check == True:
            #     print("king location:",kingLocation)
            #     print("source piece location",sourcePiece.location)
            #     print("displacement", displacement)
            try:
                for x, y in diagonal:
                    for step in (range(1, abs(int(displacement[0]) + 1))):
                        # print("x: ", str(sourcePiece.location[0] + (x * int(step))))
                        # print("y: ",str(sourcePiece.location[1] + (y * int(step))))
                        for piece in pieces:
                            if (int(piece.location[0]) == int(sourcePiece.location[0] + (x * step)) and int(piece.location[1]) == int(sourcePiece.location[1] + (y * step))):
                                # print("targetPiece: ", piece.displayValue)
                                # print("targetPiece location: ", piece.location)
                                if check == True and sourcePiece.side != piece.side: 
                                    if piece.displayValue == "wk" or piece.displayValue == "bk":
                                        return "check"
                                    else:
                                        return False
                                elif sourcePiece != piece and sourcePiece.side == piece.side:
                                    # print(sourcePiece.location)
                                    # print(piece.displayValue)
                                    # print(piece.location)
                                    return True
            except:
                return -1
        return False

    def checkValidator(self, sourcePiece, king, player):
        #calculate displacement
        displacement = []
        displacement.append(int(king.location[0]) - int(sourcePiece.location[0]))
        displacement.append(int(king.location[1]) - int(sourcePiece.location[1]))       

        if sourcePiece.perpendicular == True and sourcePiece.diagonal == True:
            #specifically for queen
            #east
            if displacement[0] > 0 and displacement[1] == 0:
                orthogonal = [1,0]
            #west
            elif displacement[0] < 0 and displacement[1] == 0:
                orthogonal = [-1,0]
            #north
            elif displacement[1] < 0 and displacement[0] == 0:
                orthogonal = [0,-1]
            #south
            elif displacement[1] > 0 and displacement[0] == 0:
                orthogonal = [0,1]
            else:
                orthogonal = ""

            #northeast
            if displacement[0] > 0 and displacement[1] < 0:
                diagonal = [(1,-1)]
            #northwest
            elif displacement[0] < 0 and displacement[1] < 0:
                diagonal = [(-1,-1)]
            #southeast
            elif displacement[0] > 0 and displacement[1] > 0:
                diagonal = [(1,1)]
            #southwest
            elif displacement[0] < 0 and displacement[1] > 0:
                diagonal = [(-1,1)]
            else:
                diagonal = ""

            try:
                #diagonal
                if diagonal != "":
                    for x, y in diagonal:
                        for step in (range(1, abs(int(displacement[0]) + 1))):
                            if (int(king.location[0]) == int(sourcePiece.location[0] + (x * step)) and int(king.location[1]) == int(sourcePiece.location[1] + (y * step))):
                                if sourcePiece.side != king.side: 
                                    return "check"
                                else:
                                    return False
                #x Axis
                if displacement[0] != 0 and orthogonal != "":
                    for step in (range(1, abs(int(displacement[0])))):
                        if int(sourcePiece.location[1]) == int(king.location[1]) and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) == int(king.location[0]) \
                        and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step)) <= sourcePiece.distance):
                            if sourcePiece.side != king.side: 
                                return "check"
                            else:
                                return False

                #y Axis
                elif displacement[1] != 0 and orthogonal != "":
                    for step in (range(1, abs(int(displacement[1])))):
                        if int(sourcePiece.location[0]) == int(king.location[0]) and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) == int(king.location[1]) \
                        and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step)) <= sourcePiece.distance):
                            if sourcePiece.side != king.side: 
                                return "check"
                            else:
                                return False
            except:
                return -1

        elif sourcePiece.perpendicular == True and sourcePiece.diagonal == False:       

            #east
            if displacement[0] > 0 and displacement[1] == 0:
                orthogonal = [1,0]
            #west
            elif displacement[0] < 0 and displacement[1] == 0:
                orthogonal = [-1,0]
            #north
            elif displacement[1] < 0 and displacement[0] == 0:
                orthogonal = [0,-1]
            #south
            elif displacement[1] > 0 and displacement[0] == 0:
                orthogonal = [0,1]
            else:
                orthogonal = ""

            #x Axis
            if displacement[0] != 0 and orthogonal != "":
                for step in (range(1, abs(int(displacement[0])))):
                    if int(sourcePiece.location[1]) == int(king.location[1]) and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) == int(king.location[0]) \
                    and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step)) <= sourcePiece.distance):
                        if sourcePiece.side != king.side: 
                            return "check"
                        else:
                            return False

            #y Axis
            elif displacement[1] != 0 and orthogonal != "":
                for step in (range(1, abs(int(displacement[1])))):
                    if int(sourcePiece.location[0]) == int(king.location[0]) and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) == int(king.location[1]) \
                    and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step)) <= sourcePiece.distance):
                        if sourcePiece.side != king.side: 
                            return "check"
                        else:
                            return False

        elif sourcePiece.diagonal == True and sourcePiece.perpendicular == False:
            #northeast
            if displacement[0] > 0 and displacement[1] < 0:
                diagonal = [(1,-1)]
            #northwest
            elif displacement[0] < 0 and displacement[1] < 0:
                diagonal = [(-1,-1)]
            #southeast
            elif displacement[0] > 0 and displacement[1] > 0:
                diagonal = [(1,1)]
            #southwest
            elif displacement[0] < 0 and displacement[1] > 0:
                diagonal = [(-1,1)]
            else:
                diagonal = ""
            
            try:
                for x, y in diagonal:
                    for step in (range(1, abs(int(displacement[0]) + 1))):
                        if (int(king.location[0]) == int(sourcePiece.location[0] + (x * step)) and int(king.location[1]) == int(sourcePiece.location[1] + (y * step))):
                            if sourcePiece.side != king.side: 
                                return "check"
                            else:
                                return False
            except:
                return -1
        return False

    def allyChecker(self, pieces, currentPlayer, sanitizedDestination):
        for piece in pieces:
            location = piece.location

            if int(sanitizedDestination[0]) == int(location[0]) and int(sanitizedDestination[1]) == int(location[1]):
                side = piece.side
                if currentPlayer.side == side:
                    return True
                else:
                    return piece
        return False

    def check(self, pieces, player):
        for piece in pieces:
            index = pieces.index(piece)
            if player.side != piece.side and (piece.displayValue == "wk" or piece.displayValue == "bk"):
                enemyKingLocation = pieces[index].location
                enemyKing = piece
                # print("enemy king location: ", enemyKingLocation)
                # print(enemyKing.displayValue)
                
        #need to not stop once return value is provided. Need to check all pieces for existance of check
        for piece in pieces:
            #isCheck = createdBoard.collisionChecker(pieces, piece, enemyKingLocation, True, player)  
            isCheck = createdBoard.checkValidator(piece, enemyKing, player)
            if isCheck == "check":
                return "check", enemyKing.side
        return False, enemyKing.side

def clearScreen():
    os.system('clear')

def parser(coordinates, reverse):
    chessRank = {"a":"0", "b":"1", "c":"2", "d":"3", "e":"4", "f":"5", "g":"6", "h":"7"}
    chessFile = {"1":"7", "2":"6", "3":"5", "4":"4", "5":"3", "6":"2", "7":"1", "8":"0"}
    reverseChessFile = {"7":"1", "6":"2", "5":"3", "4":"4", "3":"5", "2":"6", "1":"7", "0":"8"}
    noSpaceString = str(coordinates).replace(" ", "")
    parsedString = str(noSpaceString).split(",")
    pattern = "[a-h]"
    parsedCoordinates = []

    try:
        if int(parsedString[1]) > 8 or int(parsedString[1]) < 0:
            return False
        else:
            if re.match(pattern, parsedString[0]):
                parsedCoordinates.append(int(chessRank[parsedString[0]]))
                if reverse == True:
                    parsedCoordinates.append(int(reverseChessFile[parsedString[1]]))
                else:
                    parsedCoordinates.append(int(chessFile[parsedString[1]]))
                return parsedCoordinates
            else:
                parsedCoordinates.append(parsedString[0])
                if reverse == True:
                    parsedCoordinates.append(int(reverseChessFile[parsedString[1]]))
                else:
                    parsedCoordinates.append(int(chessFile[parsedString[1]]))
                return parsedCoordinates
    except:
        return False

class Player1():
    def __init__(self, name, side, points):
        self.name = name
        self.points = points
        self.side = side

class Player2():
    def __init__(self, name, side, points):
        self.name = name
        self.points = points
        self.side = side

def Game(createdBoard, player1, player2):
    turn = 1
    winner = False
    underCheck = None
    checkingPlayer = None
    while winner != True:
        #clearScreen()
        
        #Iterate Players
        if (turn % 2) == 1:
            currentPlayer = player1
        elif (turn % 2) == 0:
            currentPlayer = player2
        else:
            print("turn error!")
        #remove once you have actual game logic
        #winner = True
        
        #start turn
        print("under Check: ", underCheck)
        if underCheck != None:
            print("CHECK!")
        print("Turn " + str(turn))
        print(currentPlayer.name + '\'s Turn')
        print(createdBoard.displayBoard(createdBoard.board))

        while True:
            sourcePiece = None
            source = input("Please provide source coordinates of the piece you want to move[x, y]: ")
            sanitizedSource = parser(source, False)
            #print("source" + str(sanitizedSource))
            if sanitizedSource == False:
                print("Incorrect Source Coordinates, Please Try Again")
                continue
            else:
                for piece in createdBoard.pieces:
                    location = piece.location
                    if int(sanitizedSource[0]) == int(location[0]) and int(sanitizedSource[1]) == int(location[1]):
                        sourcePiece = piece               
                if sourcePiece == None:
                    print("Piece not found!")
                    continue
                else:
                    side = sourcePiece.side
                    if currentPlayer.side != side:
                        print("Player does not own the piece " + str(sourcePiece.displayValue) + "!")
                        continue
                break

        while True:
            dest = input("Please provide destination coordinates of the piece you want to move[x, y]: ")
            sanitizedDestination = parser(dest, False)
            #print("destination" + str(sanitizedDestination))
            if sanitizedDestination == False:
                print("Incorrect Destination Coordinates, Please Try Again")
                continue
            else:
                #check for piece in target location
                ally = createdBoard.allyChecker(createdBoard.pieces, currentPlayer, sanitizedDestination)
                #print(ally)
                if ally == True:
                    print("Not a valid move, destination contains ally piece!")
                    continue
                elif ally != True and ally != False:
                    enemyPiece = ally
                else:
                    enemyPiece = False
                
                #check for collisions
                collision = createdBoard.collisionChecker(createdBoard.pieces, sourcePiece, sanitizedDestination, False, currentPlayer)   
                if collision == True:
                    print("Collision!")
                    continue
                elif collision == -1:
                    print("Not a valid location!")
                    continue
                # else:
                #     print("No Collision!")

                if enemyPiece == False and sourcePiece.displayValue != "bp" or sourcePiece.displayValue != "wp" and collision == False:
                    validMove = sourcePiece.move(sanitizedDestination)
                elif enemyPiece != False and sourcePiece.displayValue == "bp" or sourcePiece.displayValue == "wp" and collision == False:
                    validMove = sourcePiece.attack(sanitizedDestination)
                elif enemyPiece == False and collision == False:
                    validMove = sourcePiece.move(sanitizedDestination)
                
                if validMove == True and enemyPiece != False and collision == False:
                    createdBoard.pieces.remove(enemyPiece)
                    createdBoard.updateBoard(createdBoard.pieces)
                elif validMove == True and collision == False:
                    createdBoard.updateBoard(createdBoard.pieces)
                else:
                    print("Not a valid location for piece!")
                    continue

                while True:
                    if underCheck == None:
                        check = createdBoard.check(createdBoard.pieces, currentPlayer)

                    if check[0] == "check" and underCheck == None:
                        underCheck = check[1]
                        if currentPlayer.side != underCheck:
                            checkingPlayer = currentPlayer
                            turn += 1
                            break
                    elif check[0] == "check" and underCheck != None:                            
                        if currentPlayer.side == underCheck:
                            check = createdBoard.check(createdBoard.pieces, checkingPlayer)
                            if check[0] == "check":
                                #rollback code
                                sourcePiece.location = sanitizedSource
                                if enemyPiece != False:
                                    createdBoard.pieces.append(enemyPiece)
                                createdBoard.updateBoard(createdBoard.pieces)
                            elif check[0] != "check":
                                turn += 1
                                underCheck = None
                        break
                    else:
                        turn += 1
                        underCheck = None
                        break
                break
                

#Create pieces
#PAWNS
wp1 = Pawn("w", [0, 6], "wp", 1, True, False, 1)
wp2 = Pawn("w", [1, 6], "wp", 1, True, False, 1)
wp3 = Pawn("w", [2, 6], "wp", 1, True, False, 1)
wp4 = Pawn("w", [3, 6], "wp", 1, True, False, 1)
wp5 = Pawn("w", [4, 6], "wp", 1, True, False, 1)
wp6 = Pawn("w", [5, 6], "wp", 1, True, False, 1)
wp7 = Pawn("w", [6, 6], "wp", 1, True, False, 1)
wp8 = Pawn("w", [7, 6], "wp", 1, True, False, 1)

bp1 = Pawn("b", [0, 1], "bp", 1, True, False, 1)
bp2 = Pawn("b", [1, 1], "bp", 1, True, False, 1)
bp3 = Pawn("b", [2, 1], "bp", 1, True, False, 1)
bp4 = Pawn("b", [3, 1], "bp", 1, True, False, 1)
bp5 = Pawn("b", [4, 1], "bp", 1, True, False, 1)
bp6 = Pawn("b", [5, 1], "bp", 1, True, False, 1)
bp7 = Pawn("b", [6, 1], "bp", 1, True, False, 1)
bp8 = Pawn("b", [7, 1], "bp", 1, True, False, 1)

#THE REST
wr = Rook("w", [0, 7], "wr", 5, True, False, 7)
wkn = Knight("w", [1, 7], "wn", 3, False, False, 0)
wb = Bishop("w", [2, 7], "wb", 3, False, True, 7)
wq = Queen("w", [3, 7], "wq", 9, True, True, 7)
wk = King("w", [4, 7], "wk", 99999, True, True, 1)
wb2 = Bishop("w", [5, 7], "wb", 3, False, True, 7)
wkn2 = Knight("w", [6, 7], "wn", 3, False, False, 0)
wr2 = Rook("w", [7, 7], "wr", 5, True, False, 7)

br = Rook("b", [0, 0], "br", 5, True, False, 7)
bkn = Knight("b", [1, 0], "bn", 3, False, False, 0)
bb = Bishop("b", [2, 0], "bb", 3, False, True, 7)
bq = Queen("b", [3, 0], "bq", 9, True, True, 7)
bk = King("b", [4, 0], "bk", 99999, True, True, 1)
bb2 = Bishop("b", [5, 0], "bb", 3, False, True, 7)
bkn2 = Knight("b", [6, 0], "bn", 3, False, False, 0)
br2 = Rook("b", [7, 0], "br", 5, True, False, 7)

player1 = Player1("player1111","w", 0)
player2 = Player2("player2222","b", 0)
createdBoard = Chess_Board([bp1, wp1, bp2, wp2, bp3, wp3, bp4, wp4, bp5, wp5, bp6, wp6, bp7, wp7, bp8, wp8, br, wr, bkn, wkn, bb, wb, bq, wq, bk, wk, bb2, wb2, bkn2, wkn2, br2, wr2])

Game(createdBoard, player1, player2)