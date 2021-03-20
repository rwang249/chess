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

class Piece():
    #initalize piece
    def __init__(self, location, displayValue):
        self.location = location
        self.displayValue = displayValue
        
class Pawn(Piece):
    #define movement to pass to move
    def __init__(self, side, location, displayValue, scoreValue, perpendicular, diagonal, distance):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue
        self.perpendicular = perpendicular
        self.diagonal = diagonal
        self.firstMoveUsed = False
        self.distance = distance

    def move(self, targetLocation):
        #used only for first move of a pawn
        if self.firstMoveUsed == False:
            if self.side == "b":
                if int(targetLocation[1]) == int(self.location[1]) + 1 or int(targetLocation[1]) == int(self.location[1]) + 2 and int(targetLocation[0]) == int(self.location[0]):
                    self.location[1] = int(targetLocation[1])
                    self.firstMoveUsed = True
                    return True
                else:
                    return False
            elif self.side == "w":
                if int(targetLocation[1]) == int(self.location[1]) - 1 or int(targetLocation[1]) == int(self.location[1]) - 2 and int(targetLocation[0]) == int(self.location[0]):
                    self.location[1] = int(targetLocation[1])
                    self.firstMoveUsed = True
                    return True
                else:
                    return False

        #used for subsequent moves beyond the first
        if self.side == "b":
            if int(targetLocation[1]) == int(self.location[1]) + 1 and int(targetLocation[0]) == int(self.location[0]):
                self.location[1] = int(targetLocation[1])
                return True
            else:
                return False
        elif self.side == "w":
            if int(targetLocation[1]) == int(self.location[1]) - 1 and int(targetLocation[0]) == int(self.location[0]):
                self.location[1] = int(targetLocation[1])
                return True
            else:
                return False

    def attack(self, targetLocation):
        #method used only for pawns
        if self.side == "b":
            if int(targetLocation[1]) == int(self.location[1]) + 1 and int(targetLocation[0]) == int(self.location[0]) + 1 or int(targetLocation[0]) == int(self.location[0]) - 1:
                self.location[0] = int(targetLocation[0])
                self.location[1] = int(targetLocation[1])
                return True
            else:
                return False
        elif self.side == "w":
            if int(targetLocation[1]) == int(self.location[1]) - 1 and int(targetLocation[0]) == int(self.location[0]) + 1 or int(targetLocation[0]) == int(self.location[0]) - 1:
                self.location[0] = int(targetLocation[0])
                self.location[1] = int(targetLocation[1])
                return True
            else:
                return False

class Knight(Piece):
    def __init__(self, side, location, displayValue, scoreValue , perpendicular, diagonal, distance):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue
        self.perpendicular = perpendicular
        self.diagonal = diagonal
        self.distance = distance

    #define movement to pass to move
    def move(self, targetLocation):
        valid = False
        if int(targetLocation[1]) == int(self.location[1]) + 2 or int(targetLocation[1]) == int(self.location[1]) - 2: 
            if int(targetLocation[0]) == int(self.location[0] + 1) or int(targetLocation[0]) == int(self.location[0] - 1):
                valid = True
            else:
                valid = False
        elif int(targetLocation[0]) == int(self.location[0]) + 2 or int(targetLocation[0]) == int(self.location[0]) - 2:
            if int(targetLocation[1]) == int(self.location[1] + 1) or int(targetLocation[1]) == int(self.location[1] - 1):
                valid = True
            else:
                valid = False
            
        if valid == True:
            self.location[0] = int(targetLocation[0])
            self.location[1] = int(targetLocation[1])
            return True
        else:
            return False

class Rook(Piece):
    def __init__(self, side, location, displayValue, scoreValue, perpendicular, diagonal, distance):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue
        self.perpendicular = perpendicular
        self.diagonal = diagonal
        self.distance = distance

    #define movement to pass to move
    def move(self, targetLocation):
        if int(targetLocation[0]) <= 7 and int(targetLocation[1]) == self.location[1]:
            self.location[0] = int(targetLocation[0])
            self.location[1] = int(targetLocation[1])
            return True
        elif int(targetLocation[1]) <= 7 and int(targetLocation[0]) == self.location[0]: 
            self.location[0] = int(targetLocation[0])
            self.location[1] = int(targetLocation[1])
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, side, location, displayValue, scoreValue, perpendicular, diagonal, distance):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue
        self.perpendicular = perpendicular
        self.diagonal = diagonal
        self.distance = distance

    #define movement to pass to move
    ##########finish movement
    def move(self, targetLocation):
        diagonal = [(1,1),(-1,1),(1,-1),(-1,-1)]
        #perpendicular
        if int(targetLocation[0]) <= 7 and int(targetLocation[1]) == self.location[1]:
            self.location[0] = int(targetLocation[0])
            self.location[1] = int(targetLocation[1])
            return True
        elif int(targetLocation[1]) <= 7 and int(targetLocation[0]) == self.location[0]: 
            self.location[0] = int(targetLocation[0])
            self.location[1] = int(targetLocation[1])
            return True
        
        #diagonal
        for x, y in diagonal:
            for step in range(1, 7):
                if int(targetLocation[0]) == int(self.location[0]) + int(x * step) and int(targetLocation[1]) == int(self.location[1]) + int(y * step):
                    self.location[0] = int(targetLocation[0])
                    self.location[1] = int(targetLocation[1])
                    return True
        return False

class Bishop(Piece):
    def __init__(self, side, location, displayValue, scoreValue, perpendicular, diagonal, distance):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue
        self.perpendicular = perpendicular
        self.diagonal = diagonal
        self.distance = distance

    #define movement to pass to move
    def move(self, targetLocation):
        diagonal = [(1,1),(-1,1),(1,-1),(-1,-1)]
        
        #diagonal
        for x, y in diagonal:
            for step in range(1, 7):
                if int(targetLocation[0]) == int(self.location[0]) + int(x * step) and int(targetLocation[1]) == int(self.location[1]) + int(y * step):
                    self.location[0] = int(targetLocation[0])
                    self.location[1] = int(targetLocation[1])
                    return True
        return False

class King(Piece):
    def __init__(self, side, location, displayValue, scoreValue, perpendicular, diagonal, distance):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue
        self.perpendicular = perpendicular
        self.diagonal = diagonal
        self.distance = distance

    #define movement to pass to move
    def move(self, targetLocation):
        print('placeholder for move')

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

    def collisionChecker(self, pieces, sourcePiece, destination):
        #### finish for diagonal#####
        #calculate displacement
        displacement = []
        displacement.append(int(destination[0]) - int(sourcePiece.location[0]))
        displacement.append(int(destination[1]) - int(sourcePiece.location[1]))
        occurrence = 0

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
                        for step in (range(1, abs(int(displacement[0])))):
                            # print("x: ", str(sourcePiece.location[0] - (x * int(step))))
                            # print("y: ",str(sourcePiece.location[1] - (y * int(step))))
                            for piece in pieces:
                                if (int(piece.location[0]) == int(sourcePiece.location[0] + (x * step)) and int(piece.location[1]) == int(sourcePiece.location[1] + (y * step)) \
                                and diagDirection == "northeast" and sourcePiece != piece and sourcePiece.side == piece.side):
                                    print(sourcePiece.location)
                                    print(piece.displayValue)
                                    print(piece.location)
                                    return True
                #x Axis
                if displacement[0] != 0 and orthogonal != "":
                    for step in (range(abs(int(displacement[0] + 1)))):
                        for piece in pieces:
                            if int(sourcePiece.location[1]) == int(piece.location[1]) and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) == int(piece.location[0]) \
                            and piece != sourcePiece:
                                if sourcePiece.side == piece.side:
                                    return True
                                elif sourcePiece.side != piece.side:
                                    return True
                            
                #y Axis
                elif displacement[1] != 0 and orthogonal != "":
                    for step in (range(1, abs(int(displacement[1])))):
                        for piece in pieces:
                            if int(sourcePiece.location[0]) == int(piece.location[0]) and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) == int(piece.location[1]) \
                            and piece != sourcePiece:
                                if sourcePiece.side == piece.side:
                                    return True
                                elif sourcePiece.side != piece.side:
                                    return True
            except:
                return -1
            
            # print(diagDirection)
            # print(displacement)
            # print(sourcePiece.location)
            # print("diagonal", diagonal)

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

###############PREVENT PIECES TO JUMP ENEMY PIECES#############
            #x Axis
            if displacement[0] != 0 and orthogonal != "":
                for step in (range(abs(int(displacement[0] + 1)))):
                    for piece in pieces:
                        if int(sourcePiece.location[1]) == int(piece.location[1]) and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) == int(piece.location[0]) \
                        and piece != sourcePiece:
                            if sourcePiece.side == piece.side:
                                return True
                            elif sourcePiece.side != piece.side:
                                return True
                        
            #y Axis
            elif displacement[1] != 0 and orthogonal != "":
                for step in (range(1, abs(int(displacement[1])))):
                    for piece in pieces:
                        if int(sourcePiece.location[0]) == int(piece.location[0]) and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) == int(piece.location[1]) \
                        and piece != sourcePiece:
                            if sourcePiece.side == piece.side:
                                return True
                            elif sourcePiece.side != piece.side:
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
            
            # print(diagDirection)
            # print(displacement)
            # print(sourcePiece.location)
            # print("diagonal", diagonal)

            try:
                for x, y in diagonal:
                    for step in (range(1, abs(int(displacement[0])))):
                        # print("x: ", str(sourcePiece.location[0] - (x * int(step))))
                        # print("y: ",str(sourcePiece.location[1] - (y * int(step))))
                        for piece in pieces:
                            if (int(piece.location[0]) == int(sourcePiece.location[0] + (x * step)) and int(piece.location[1]) == int(sourcePiece.location[1] + (y * step)) \
                            and diagDirection == "northeast" and sourcePiece != piece and sourcePiece.side == piece.side):
                                print(sourcePiece.location)
                                print(piece.displayValue)
                                print(piece.location)
                                return True
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

def clearScreen():
    os.system('clear')

def parser(coordinates):
    chessRank = {"a":"0", "b":"1", "c":"2", "d":"3", "e":"4", "f":"5", "g":"6", "h":"7"}
    chessFile = {"1":"7", "2":"6", "3":"5", "4":"4", "5":"3", "6":"2", "7":"1", "8":"0"}
    string = re.sub('[\[!@#%$\s+\][i-z][A-Z],', '', coordinates)
    pattern = "[a-h]"
    parsedCoordinates = []

    try:
        if int(coordinates[3]) > 8 or int(coordinates[3]) < 0:
            return False
        else:
            if re.match(pattern, coordinates[0]):
                parsedCoordinates.append(chessRank[coordinates[0]])
                parsedCoordinates.append(chessFile[coordinates[3]])
                return parsedCoordinates
            else:
                parsedCoordinates.append(coordinates[0])
                parsedCoordinates.append(chessFile[coordinates[3]])
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
    chessFile = {"1":"7", "2":"6", "3":"5", "4":"4", "5":"3", "6":"2", "7":"1", "8":"0"}
    turn = 1
    winner = False
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
        print("Turn " + str(turn))
        print(currentPlayer.name + '\'s Turn')
        print(createdBoard.displayBoard(createdBoard.board))
        while True:
            sourcePiece = None
            source = input("Please provide source coordinates of the piece you want to move[x, y]: ")
            sanitizedSource = parser(source)
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
            sanitizedDestination = parser(dest)
            #print("destination" + str(sanitizedDestination))
            #print("source piece location" + str(sourcePiece.location))

            if sanitizedDestination == False:
                print("Incorrect Destination Coordinates, Please Try Again")
                continue
            else:
                #check for piece in target location
                ally = createdBoard.allyChecker(createdBoard.pieces, currentPlayer, sanitizedDestination)
                print(ally)
                if ally == True:
                    print("Not a valid move, destination contains ally piece!")
                    continue
                elif ally != True and ally != False:
                    enemyPiece = ally
                else:
                    enemyPiece = False
                
                #check for collisions
                collision = createdBoard.collisionChecker(createdBoard.pieces, sourcePiece, sanitizedDestination)   
                if collision == True:
                    print("Collision!")
                    continue
                elif collision == -1:
                    print("Not a valid location!")
                    continue
                else:
                    print("No Collision!")

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
                break
        turn += 1

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