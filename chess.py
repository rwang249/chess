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

class Piece():
    #initalize piece
    def __init__(self, location, displayValue):
        #startLocation = location
        #print(location)
        self.location = location
        self.displayValue = displayValue
        
class Pawn(Piece):
    #define movement to pass to move
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue
        self.firstMoveUsed = False

    def move(self, targetLocation):
        #########fix move for pawn############
        #used only for first move of a pawn
        if targetLocation == self.location:
            if self.side == "b":
                if targetLocation[1] == self.location[1] - 2 or targetLocation[1] == self.location[1] - 2:
                    return True
                else:
                    return False
            elif self.side == "w":
                if targetLocation[1] == self.location[1] + 2 or targetLocation[1] == self.location[1] - 2:
                    return True
                else:
                    return False

        #used for subsequent moves beyond the first
        if self.side == "b":
            if targetLocation[1] == self.location[1] - 1:
                return True
            else:
                return False
        elif self.side == "w":
            if targetLocation[1] == self.location[1] + 1:
                return True
            else:
                return False

class Knight(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class Rook(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class Queen(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class Bishop(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class King(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue

    #define movement to pass to move
    def move(self):
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
            #print(pieces[index].side, pieces[index].location, pieces[index].displayValue, pieces[index].scoreValue)
        #self.displayBoard(board)
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
    turn = 1
    winner = False
    while winner != True:

        clearScreen()
        
        #Iterate Players
        if (turn % 2) == 1:
            currentPlayer = player1
        elif (turn % 2) == 0:
            currentPlayer = player2
        else:
            print("turn error!")
        #remove once you have actual game logic
        winner = True

        ####################
        #REFERENCE
        # for piece in createdBoard.pieces:
        #     index = createdBoard.pieces.index(piece)
        #     pieceLocation = createdBoard.pieces[index].location
        #     print(createdBoard.pieces[index].location)
        ##############################
        
        #start turn
        print("Turn " + str(turn))
        print(currentPlayer.name + '\'s Turn')
        print(createdBoard.displayBoard(createdBoard.board))
        while True:
            sourcePiece = None
            source = input("Please provide source coordinates of the piece you want to move[x, y]: ")
            sanitizedSource = parser(source)
            print(sanitizedSource)
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
            source = input("Please provide destination coordinates of the piece you want to move[x, y]: ")
            sanitizedDestination = parser(source)
            if sanitizedDestination == False:
                print("Incorrect Destination Coordinates, Please Try Again")
                continue
            else:
                for piece in createdBoard.pieces:
                    location = piece.location
                    if int(sanitizedDestination[0]) == int(location[0]) and int(sanitizedDestination[1]) == int(location[1]):
                        side = piece.side
                        if currentPlayer.side == side:
                            print("Not a valid move, destination contains ally piece!")
                        else:
                        ################################work on next####################
                            piece.move()
                break
        
        print('source: ' + str(sanitizedSource))
        print('destination: ' + str(sanitizedDestination))

        turn += 1

#Create pieces
#PAWNS
wp1 = Pawn("w", [0, 6], "wp", 1)
wp2 = Pawn("w", [1, 6], "wp", 1)
wp3 = Pawn("w", [2, 6], "wp", 1)
wp4 = Pawn("w", [3, 6], "wp", 1)
wp5 = Pawn("w", [4, 6], "wp", 1)
wp6 = Pawn("w", [5, 6], "wp", 1)
wp7 = Pawn("w", [6, 6], "wp", 1)
wp8 = Pawn("w", [7, 6], "wp", 1)

bp1 = Pawn("b", [0, 1], "bp", 1)
bp2 = Pawn("b", [1, 1], "bp", 1)
bp3 = Pawn("b", [2, 1], "bp", 1)
bp4 = Pawn("b", [3, 1], "bp", 1)
bp5 = Pawn("b", [4, 1], "bp", 1)
bp6 = Pawn("b", [5, 1], "bp", 1)
bp7 = Pawn("b", [6, 1], "bp", 1)
bp8 = Pawn("b", [7, 1], "bp", 1)

#THE REST
wr = Rook("w", [0, 7], "wr", 5)
wkn = Knight("w", [1, 7], "wn", 3)
wb = Bishop("w", [2, 7], "wb", 3)
wq = Queen("w", [3, 7], "wq", 9)
wk = King("w", [4, 7], "wk", 99999)
wb2 = Bishop("w", [5, 7], "wb", 3)
wkn2 = Knight("w", [6, 7], "wn", 3)
wr2 = Rook("w", [7, 7], "wr", 5)

br = Rook("b", [0, 0], "br", 5)
bkn = Knight("b", [1, 0], "bn", 3)
bb = Bishop("b", [2, 0], "bb", 3)
bq = Queen("b", [3, 0], "bq", 9)
bk = King("b", [4, 0], "bk", 99999)
bb2 = Bishop("b", [5, 0], "bb", 3)
bkn2 = Knight("b", [6, 0], "bn", 3)
br2 = Rook("b", [7, 0], "br", 5)

player1 = Player1("player1111","w", 0)
player2 = Player2("player2222","b", 0)
createdBoard = Chess_Board([bp1, wp1, bp2, wp2, bp3, wp3, bp4, wp4, bp5, wp5, bp6, wp6, bp7, wp7, bp8, wp8, br, wr, bkn, wkn, bb, wb, bq, wq, bk, wk, bb2, wb2, bkn2, wkn2, br2, wr2])

Game(createdBoard, player1, player2)