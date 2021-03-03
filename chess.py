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
        startLocation = location
        print(location)
        
class Pawn(Piece):
    #define movement to pass to move
    def __init__(self, side, location, displayValue, scoreValue):
        super().__init__(location, displayValue)

    def move(self):
        print('placeholder for move')

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
    def __init__(self):
        board = []
        for row in range(8):
            column = []
            board.append(column)
            for columnNum in range(8):
                column.append('.')
        board[0][7] = 'pawn'
        #board[1][2] = 'pawn'
        print(board)
        #self.displayBoard(board)
        
    def displayBoard(self, board):
        rowNum = 8
        print("  ", end="")
        for row in board:
            print("-" * 41)
            print(str(rowNum), end=" ")
            rowNum -= 1
            for column in row:
                print("|{}".format(column), end="")
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
bp1 = Pawn("b", [0, 6], "bp", 1)
wp1 = Pawn("w", [0, 1], "wp", 1)
bp2 = Pawn("b", [1, 6], "bp", 1)
wp2 = Pawn("w", [1, 1], "wp", 1)
bp3 = Pawn("b", [2, 6], "bp", 1)
wp3 = Pawn("w", [2, 1], "wp", 1)
bp4 = Pawn("b", [3, 6], "bp", 1)
wp4 = Pawn("w", [3, 1], "wp", 1)
bp5 = Pawn("b", [4, 6], "bp", 1)
wp5 = Pawn("w", [4, 1], "wp", 1)
bp6 = Pawn("b", [5, 6], "bp", 1)
wp6 = Pawn("w", [5, 1], "wp", 1)
bp7 = Pawn("b", [6, 6], "bp", 1)
wp7 = Pawn("w", [6, 1], "wp", 1)
bp8 = Pawn("b", [7, 6], "bp", 1)
wp8 = Pawn("w", [7, 1], "wp", 1)

#THE REST
br = Rook("b", [0, 7], "br", 5)
wr = Rook("w", [0, 0], "wr", 5)
bkn = Knight("b", [1, 7], "bkn", 3)
wkn = Knight("w", [1, 0], "wkn", 3)
bb = Bishop("b", [2, 7], "bb", 3)
wb = Bishop("w", [2, 0], "wb", 3)
bq = Queen("b", [3, 7], "bq", 9)
wq = Queen("w", [3, 0], "wq", 9)
bk = King("b", [4, 7], "bk", 99999)
wk = King("w", [4, 0], "wk", 99999)
bb2 = Bishop("b", [5, 7], "bb2", 3)
wb2 = Bishop("w", [5, 0], "wb2", 3)
bkn2 = Knight("b", [6, 7], "bkn2", 3)
wkn2 = Knight("w", [6, 0], "wkn2", 3)
br2 = Rook("b", [7, 7], "br2", 5)
wr2 = Rook("w", [7, 0], "wr2", 5)


board = Chess_Board()















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
