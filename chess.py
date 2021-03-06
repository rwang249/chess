#!/usr/bin/env python3

#use inheritance(i.e. board should refer to pieces, and pieces should refer to specific piece's common method(movement))
#use abstraction
#create method to check status of gameboard
#create class to for board
#create class for pieces
#base class of piece
#derivative will be individual pieces
#chess board composition of piece?

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
        self.side = side
        self.location = location
        self.displayValue = displayValue
        self.scoreValue = scoreValue
        super().__init__(location, displayValue)

    def move(self):
        if self.side = "b":
            self.location[1] -= 1
        elif self.side = "w":
            self.location[1] += 1

class Knight(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class Rook(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class Queen(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class Bishop(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class King(Piece):
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)

    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class Chess_Board():
    def __init__(self, pieces):
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
        self.displayBoard(board)

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


# Pawn: 1 point (or pawn)
# Knight: 3 points.
# Bishop: 3 points.
# Rook: 5 points.
# Queen: 9 points
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

board = Chess_Board([bp1, wp1, bp2, wp2, bp3, wp3, bp4, wp4, bp5, wp5, bp6, wp6, bp7, wp7, bp8, wp8, br, wr, bkn, wkn, bb, wb, bq, wq, bk, wk, bb2, wb2, bkn2, wkn2, br2, wr2])















# class Chess_Board():
#     def __init__(self):
#         board = [['    '] * 8] * 8
#         self.displayBoard(board)
        
#     def displayBoard(self, board):
#         rowNum = 8
#         print("  ", end="")
#         for row in board:
#             print("-" * 41)
#             print(str(rowNum), end=" ")
#             rowNum -= 1
#             for column in row:
#                 print("|{}".format(column), end="")
#             print("|")
#             print("  ", end="")
#         print("-" * 41)
#         for letter in ["a", "b", "c", "d", "e", "f", "g", "h"]:
#             print("   {} ".format(letter), end="")
#         print("\n")
