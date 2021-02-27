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
    def __init__(self, side, startingLocation, displayValue, scoreValue):
        print('test')
        
class Pawn(Piece):
    #define movement to pass to move
    def move(self):
        print('placeholder for move')

class Chess_Board():
    def __init__(self):
        board = [['    '] * 8] * 8
        self.displayBoard(board)
        
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
bp = Piece(self, "b", [x, 7], bp, 1)
wp = Piece(self, "w", [x, 2], wp, 1)
br = Piece(self, "b", [1, 8], br, 5)
wr = Piece(self, "w", [1, 1], wr, 5)
bkn = Piece(self, "b", [2, 8], bkn, 3)
wkn = Piece(self, "w", [2, 1], wkn, 3)
bb = Piece(self, "b", [3, 8], bb, 3)
wb = Piece(self, "w", [3, 1], wb, 3)
bq = Piece(self, "b", [4, 8], bq, 9)
wq = Piece(self, "w", [4, 1], wq, 9)
bk = Piece(self, "b", [5, 8], bk, 99999)
wk = Piece(self, "w", [5, 1], wk, 99999)
bb2 = Piece(self, "b", [6, 8], bb2, 3)
wb2 = Piece(self, "w", [6, 1], wb2, 3)
bkn2 = Piece(self, "b", [7, 8], bkn2, 3)
wkn2 = Piece(self, "w", [7, 1], wkn2, 3)
br2 = Piece(self, "b", [8, 8], br2, 5)
wr2 = Piece(self, "w", [8, 1], wr2, 5)


board = Chess_Board()
