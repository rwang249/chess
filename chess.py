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
        global positions
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
            #print(pieceLocation)
            #parsedLocation = self.parser(str(pieceLocation), False)
            #print(parsedLocation)
            position = {str(pieceLocation): pieces[index].displayValue} 
            positions.update(position)
            board[pieceLocation[1]][pieceLocation[0]] = str(pieces[index].displayValue).format()
        self.board = board
        #print(positions)

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
                #diagonal
                if diagonal != "":
                    for x, y in diagonal:
                        for step in (range(1, abs(int(displacement[0]) + 1))):
                            for piece in pieces:
                                if (int(piece.location[0]) == int(sourcePiece.location[0] + (x * step)) and int(piece.location[1]) == int(sourcePiece.location[1] + (y * step)) \
                                and sourcePiece != piece and sourcePiece.side == piece.side):
                                    return True

                #x Axis
                if displacement[0] != 0 and orthogonal != "":
                    for step in (range(1, abs(int(displacement[0])))):
                        for piece in pieces:
                            if int(sourcePiece.location[1]) == int(piece.location[1]) and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) == int(piece.location[0]) \
                            and ((int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) <= piece.distance):
                                if sourcePiece.side == piece.side:
                                    return True
                                elif sourcePiece.side != piece.side:
                                    return True

                #y Axis
                elif displacement[1] != 0 and orthogonal != "":
                    for step in (range(1, abs(int(displacement[1])))):
                        for piece in pieces:
                            if int(sourcePiece.location[0]) == int(piece.location[0]) and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) == int(piece.location[1]) \
                            and ((int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) <= piece.distance):
                                if sourcePiece.side == piece.side:
                                    return True
                                elif sourcePiece.side != piece.side:
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

            #x Axis
            if displacement[0] != 0 and orthogonal != "":
                for step in (range(1, abs(int(displacement[0])))):
                    for piece in pieces:
                        if int(sourcePiece.location[1]) == int(piece.location[1]) and (int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) == int(piece.location[0]) \
                        and ((int(sourcePiece.location[0] + (int(orthogonal[0]) * step))) <= piece.distance):
                            if sourcePiece.side == piece.side:
                                return True
                            elif sourcePiece.side != piece.side:
                                return True

            #y Axis
            elif displacement[1] != 0 and orthogonal != "":
                for step in (range(1, abs(int(displacement[1])))):
                    for piece in pieces:
                        if int(sourcePiece.location[0]) == int(piece.location[0]) and (int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) == int(piece.location[1]) \
                        and ((int(sourcePiece.location[1] + (int(orthogonal[1]) * step))) <= piece.distance):
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
            
            try:
                for x, y in diagonal:
                    for step in (range(1, abs(int(displacement[0]) + 1))):
                        for piece in pieces:
                            if (int(piece.location[0]) == int(sourcePiece.location[0] + (x * step)) and int(piece.location[1]) == int(sourcePiece.location[1] + (y * step)) \
                            and sourcePiece != piece and sourcePiece.side == piece.side):
                                return True
            except:
                return -1
        return False

    def checkValidator(self, sourcePiece, king, player):
        #think about implementing a dictionary to avoid O(N) for searching for location 
        global positions
        kingFound = False
        pieceFound = False
        unprotected = False

        #calculate displacement
        displacement = []
        displacement.append(int(king.location[0]) - int(sourcePiece.location[0]))
        displacement.append(int(king.location[1]) - int(sourcePiece.location[1]))

        #pawns
        if sourcePiece.perpendicular == True and sourcePiece.diagonal == False and (sourcePiece.displayValue == "wp" or sourcePiece.displayValue == "bp"):
            if sourcePiece.displayValue == "wp":
                position1 = '[{0}, {1}]'.format(str(sourcePiece.location[0] + 1), str(sourcePiece.location[1] - 1))
                position2 = '[{0}, {1}]'.format(str(sourcePiece.location[0] - 1), str(sourcePiece.location[1] - 1))
                position1Piece = positions.get(position1)
                position2Piece = positions.get(position2)
                if position1Piece == king.displayValue:
                    kingFound = True
                    unprotected = True
                elif position2Piece == king.displayValue:
                    kingFound = True
                    unprotected = True
            elif sourcePiece.displayValue == "bp":
                position1 = '[{0}, {1}]'.format(str(sourcePiece.location[0] + 1), str(sourcePiece.location[1] + 1))
                position2 = '[{0}, {1}]'.format(str(sourcePiece.location[0] - 1), str(sourcePiece.location[1] + 1))
                position1Piece = positions.get(position1)
                position2Piece = positions.get(position2)
                if position1Piece == king.displayValue:
                    kingFound = True
                    unprotected = True
                elif position2Piece == king.displayValue:
                    kingFound = True
                    unprotected = True

        #knights
        elif sourcePiece.perpendicular == False and sourcePiece.diagonal == False:
            print("placeholder")

        #queen and king
        elif sourcePiece.perpendicular == True and sourcePiece.diagonal == True:
            eastOrthogonal = [1,0]
            westOrthogonal = [-1,0]
            northOrthogonal = [0,-1]
            southOrthogonal = [0,1]

            northeastDiagonal = [(1,-1)]
            northwestDiagonal = [(-1,-1)]
            southeastDiagonal = [(1,1)]
            southwestDiagonal = [(-1,1)]

            while kingFound != True:
                if sourcePiece.side != king.side:     
                    #diagonal
                    #northeast
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        for x, y in northeastDiagonal:
                            if kingFound != True:
                                position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (x * step))), str((sourcePiece.location[1] + (y * step))))
                                piece = positions.get(position)
                                if piece != None and piece != king.displayValue:
                                    pieceFound = True
                                elif piece == king.displayValue:
                                    kingFound = True
                                    break

                                #check ahead just in case king is right behind piece
                                kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + ((x * step) + 1))), str((sourcePiece.location[1] + ((y * step) - 1))))
                                kingPiece = positions.get(kingPosition)
                                if kingPiece != None and kingPiece == king.displayValue:
                                    kingFound = True
                                    break
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break
                  

                    #northwest
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        for x, y in northwestDiagonal:
                            if kingFound != True:
                                position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (x * step))), str((sourcePiece.location[1] + (y * step))))
                                piece = positions.get(position)
                                if piece != None and piece != king.displayValue:
                                    pieceFound = True
                                elif piece == king.displayValue:
                                    kingFound = True
                                    break

                                #check ahead just in case king is right behind piece
                                kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + ((x * step) - 1))), str((sourcePiece.location[1] + ((y * step) - 1))))
                                kingPiece = positions.get(kingPosition)
                                if kingPiece != None and kingPiece == king.displayValue:
                                    kingFound = True
                                    break
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break


                    #southeast
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        for x, y in southeastDiagonal:
                            if kingFound != True:
                                position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (x * step))), str((sourcePiece.location[1] + (y * step))))
                                piece = positions.get(position)
                                if piece != None and piece != king.displayValue:
                                    pieceFound = True
                                elif piece == king.displayValue:
                                    kingFound = True
                                    break

                                #check ahead just in case king is right behind piece
                                kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + ((x * step) + 1))), str((sourcePiece.location[1] + ((y * step) + 1))))
                                kingPiece = positions.get(kingPosition)
                                if kingPiece != None and kingPiece == king.displayValue:
                                    kingFound = True
                                    break
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break


                    #southwest
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        for x, y in southwestDiagonal:
                            if kingFound != True:
                                position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (x * step))), str((sourcePiece.location[1] + (y * step))))
                                piece = positions.get(position)
                                if piece != None and piece != king.displayValue:
                                    pieceFound = True
                                elif piece == king.displayValue:
                                    kingFound = True
                                    break

                                #check ahead just in case king is right behind piece
                                kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + ((x * step) - 1))), str((sourcePiece.location[1] + ((y * step) + 1))))
                                kingPiece = positions.get(kingPosition)
                                if kingPiece != None and kingPiece == king.displayValue:
                                    kingFound = True
                                    break
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break

                    #x Axis
                    #east
                    for step in (range(1, int(sourcePiece.distance) + 1)):

                        position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (int(eastOrthogonal[0]) * step))), str(sourcePiece.location[1]))
                        piece = positions.get(position)
                        if piece != None and piece != king.displayValue:
                            pieceFound = True
                        elif piece == king.displayValue:
                            kingFound = True
                            break

                        #check ahead just in case king is right behind piece
                        kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (int(eastOrthogonal[0]) * (step - 1)))), str(sourcePiece.location[1]))
                        kingPiece = positions.get(kingPosition)
                        if kingPiece != None and kingPiece == king.displayValue:
                            kingFound = True
                            break

                    if kingFound != True:
                        pieceFound = False
                    else:
                        break

                    #west
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        
                        position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (int(westOrthogonal[0]) * step))), str(sourcePiece.location[1]))
                        piece = positions.get(position)
                        if piece != None and piece != king.displayValue:
                            pieceFound = True
                        elif piece == king.displayValue:
                            kingFound = True
                            break

                        #check ahead just in case king is right behind piece
                        kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (int(westOrthogonal[0]) * (step + 1)))), str(sourcePiece.location[1]))
                        kingPiece = positions.get(kingPosition)
                        if kingPiece != None and kingPiece == king.displayValue:
                            kingFound = True
                            break
         
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break

                    #y Axis
                    #north
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        position = '[{0}, {1}]'.format(str(sourcePiece.location[0]), str((sourcePiece.location[1] + (int(northOrthogonal[1]) * step))))
                        piece = positions.get(position)                   
                        if piece != None and piece != king.displayValue:
                            pieceFound = True
                        elif piece == king.displayValue:
                            kingFound = True
                            break

                        #check ahead just in case king is right behind piece
                        kingPosition = '[{0}, {1}]'.format(str(sourcePiece.location[0]), str((sourcePiece.location[1] + (int(northOrthogonal[1]) * (step - 1)))))
                        kingPiece = positions.get(kingPosition)
                        if kingPiece != None and kingPiece == king.displayValue:
                            kingFound = True
                            break

                    if kingFound != True:
                        pieceFound = False
                    else:
                        break

                    #south
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        position = '[{0}, {1}]'.format(str(sourcePiece.location[0]), str((sourcePiece.location[1] + (int(southOrthogonal[1]) * step))))
                        piece = positions.get(position)
                        if piece != None and piece != king.displayValue:
                            pieceFound = True
                        elif piece == king.displayValue:
                            kingFound = True
                            break

                        #check ahead just in case king is right behind piece
                        kingPosition = '[{0}, {1}]'.format(str(sourcePiece.location[0]), str((sourcePiece.location[1] + (int(southOrthogonal[1]) * (step + 1)))))
                        kingPiece = positions.get(kingPosition)
                        if kingPiece != None and kingPiece == king.displayValue:
                            kingFound = True
                            break
         
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break
                #if not in check at all
                break

            if pieceFound == True and kingFound == True:
                unprotected = False
            elif pieceFound == False and kingFound == True:
                unprotected = True
            
            # if sourcePiece.displayValue == "wq" or sourcePiece.displayValue == "bq":
            #     print("sourcepiece: ",sourcePiece.displayValue)
            #     print("target: ",king.displayValue)
            #     print("piece found: ", pieceFound)
            #     print("king found: ", kingFound)
            #     print("unprotected: ", unprotected)        

        #rooks
        elif sourcePiece.perpendicular == True and sourcePiece.diagonal == False:
            eastOrthogonal = [1,0]
            westOrthogonal = [-1,0]
            northOrthogonal = [0,-1]
            southOrthogonal = [0,1]

            while kingFound != True:
                if sourcePiece.side != king.side:            
                    #x Axis
                    #east
                    for step in (range(1, int(sourcePiece.distance) + 1)):

                        position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (int(eastOrthogonal[0]) * step))), str(sourcePiece.location[1]))
                        piece = positions.get(position)
                        if piece != None and piece != king.displayValue:
                            pieceFound = True
                        elif piece == king.displayValue:
                            kingFound = True
                            break

                        #check ahead just in case king is right behind piece
                        kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (int(eastOrthogonal[0]) * (step - 1)))), str(sourcePiece.location[1]))
                        kingPiece = positions.get(kingPosition)
                        if kingPiece != None and kingPiece == king.displayValue:
                            kingFound = True
                            break

                    if kingFound != True:
                        pieceFound = False
                    else:
                        break

                    #west
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        
                        position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (int(westOrthogonal[0]) * step))), str(sourcePiece.location[1]))
                        piece = positions.get(position)
                        if piece != None and piece != king.displayValue:
                            pieceFound = True
                        elif piece == king.displayValue:
                            kingFound = True
                            break

                        #check ahead just in case king is right behind piece
                        kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (int(westOrthogonal[0]) * (step + 1)))), str(sourcePiece.location[1]))
                        kingPiece = positions.get(kingPosition)
                        if kingPiece != None and kingPiece == king.displayValue:
                            kingFound = True
                            break
         
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break

                    #y Axis
                    #north
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        position = '[{0}, {1}]'.format(str(sourcePiece.location[0]), str((sourcePiece.location[1] + (int(northOrthogonal[1]) * step))))
                        piece = positions.get(position)                 
                        if piece != None and piece != king.displayValue:
                            pieceFound = True
                        elif piece == king.displayValue:
                            kingFound = True
                            break

                        #check ahead just in case king is right behind piece
                        kingPosition = '[{0}, {1}]'.format(str(sourcePiece.location[0]), str((sourcePiece.location[1] + (int(northOrthogonal[1]) * (step - 1)))))
                        kingPiece = positions.get(kingPosition)
                        if kingPiece != None and kingPiece == king.displayValue:
                            kingFound = True
                            break

                    if kingFound != True:
                        pieceFound = False
                    else:
                        break

                    #south
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        position = '[{0}, {1}]'.format(str(sourcePiece.location[0]), str((sourcePiece.location[1] + (int(southOrthogonal[1]) * step))))
                        piece = positions.get(position)
                        if piece != None and piece != king.displayValue:
                            pieceFound = True
                        elif piece == king.displayValue:
                            kingFound = True
                            break

                        #check ahead just in case king is right behind piece
                        kingPosition = '[{0}, {1}]'.format(str(sourcePiece.location[0]), str((sourcePiece.location[1] + (int(southOrthogonal[1]) * (step + 1)))))
                        kingPiece = positions.get(kingPosition)
                        if kingPiece != None and kingPiece == king.displayValue:
                            kingFound = True
                            break
         
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break
                break

            if pieceFound == True and kingFound == True:
                unprotected = False
            elif pieceFound == False and kingFound == True:
                unprotected = True

        #bishops
        elif sourcePiece.diagonal == True and sourcePiece.perpendicular == False:
            northeastDiagonal = [(1,-1)]
            northwestDiagonal = [(-1,-1)]
            southeastDiagonal = [(1,1)]
            southwestDiagonal = [(-1,1)]

            while kingFound != True:
                if sourcePiece.side != king.side:         
                #diagonal
                #northeast
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        for x, y in northeastDiagonal:
                            if kingFound != True:
                                position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (x * step))), str((sourcePiece.location[1] + (y * step))))
                                piece = positions.get(position)
                                if piece != None and piece != king.displayValue:
                                    pieceFound = True
                                elif piece == king.displayValue:
                                    kingFound = True
                                    break

                                #check ahead just in case king is right behind piece
                                kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + ((x * step) + 1))), str((sourcePiece.location[1] + ((y * step) - 1))))
                                kingPiece = positions.get(kingPosition)
                                if kingPiece != None and kingPiece == king.displayValue:
                                    kingFound = True
                                    break
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break
                    

                    #northwest
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        for x, y in northwestDiagonal:
                            if kingFound != True:
                                position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (x * step))), str((sourcePiece.location[1] + (y * step))))
                                piece = positions.get(position)
                                if piece != None and piece != king.displayValue:
                                    pieceFound = True
                                elif piece == king.displayValue:
                                    kingFound = True
                                    break

                                #check ahead just in case king is right behind piece
                                kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + ((x * step) - 1))), str((sourcePiece.location[1] + ((y * step) - 1))))
                                kingPiece = positions.get(kingPosition)
                                if kingPiece != None and kingPiece == king.displayValue:
                                    kingFound = True
                                    break
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break


                    #southeast
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        for x, y in southeastDiagonal:
                            if kingFound != True:
                                position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (x * step))), str((sourcePiece.location[1] + (y * step))))
                                piece = positions.get(position)
                                if piece != None and piece != king.displayValue:
                                    pieceFound = True
                                elif piece == king.displayValue:
                                    kingFound = True
                                    break

                                #check ahead just in case king is right behind piece
                                kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + ((x * step) + 1))), str((sourcePiece.location[1] + ((y * step) + 1))))
                                kingPiece = positions.get(kingPosition)
                                if kingPiece != None and kingPiece == king.displayValue:
                                    kingFound = True
                                    break
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break


                    #southwest
                    for step in (range(1, int(sourcePiece.distance) + 1)):
                        for x, y in southwestDiagonal:
                            if kingFound != True:
                                position = '[{0}, {1}]'.format(str((sourcePiece.location[0] + (x * step))), str((sourcePiece.location[1] + (y * step))))
                                piece = positions.get(position)
                                if piece != None and piece != king.displayValue:
                                    pieceFound = True
                                elif piece == king.displayValue:
                                    kingFound = True
                                    break

                                #check ahead just in case king is right behind piece
                                kingPosition = '[{0}, {1}]'.format(str((sourcePiece.location[0] + ((x * step) - 1))), str((sourcePiece.location[1] + ((y * step) + 1))))
                                kingPiece = positions.get(kingPosition)
                                if kingPiece != None and kingPiece == king.displayValue:
                                    kingFound = True
                                    break
                    if kingFound != True:
                        pieceFound = False
                    else:
                        break
                break

            if pieceFound == True and kingFound == True:
                unprotected = False
            elif pieceFound == False and kingFound == True:
                unprotected = True

        if kingFound == True and unprotected == True:
            return "check"
        else:
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
                
        #need to check all pieces for existance of check
        for x in range(len(pieces)):
            isCheck = createdBoard.checkValidator(pieces[x], enemyKing, player)
            if isCheck == "check":
                return "check", enemyKing.side
        return False, enemyKing.side

    def parser(self, coordinates, reverse):
        chessRank = {"a":"0", "b":"1", "c":"2", "d":"3", "e":"4", "f":"5", "g":"6", "h":"7"}
        chessFile = {"1":"7", "2":"6", "3":"5", "4":"4", "5":"3", "6":"2", "7":"1", "8":"0"}
        reverseChessFile = {"7":"1", "6":"2", "5":"3", "4":"4", "3":"5", "2":"6", "1":"7", "0":"8"}
        noBracketString1 = str(coordinates).replace("[", "")
        noBracketString2 = str(noBracketString1).replace("]", "")
        noSpaceString = str(noBracketString2).replace(" ", "")
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
                    parsedCoordinates.append(int(parsedString[0]))
                    if reverse == True:
                        parsedCoordinates.append(int(reverseChessFile[parsedString[1]]))
                    else:
                        parsedCoordinates.append(int(chessFile[parsedString[1]]))
                    return parsedCoordinates
        except:
            return False

def clearScreen():
    os.system('clear')

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
    global positions
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
        if underCheck != None:
            print("CHECK!")
        print("Turn " + str(turn))
        print(currentPlayer.name + '\'s Turn')
        print(createdBoard.displayBoard(createdBoard.board))

        while True:
            sourcePiece = None
            source = input("Please provide source coordinates of the piece you want to move[x, y]: ")
            sanitizedSource = createdBoard.parser(source, False)
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
            sanitizedDestination = createdBoard.parser(dest, False)
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
                    del positions[str(enemyPiece.location)]
                    del positions[str(sanitizedSource)]
                    position = {str(sourcePiece.location): sourcePiece.displayValue}
                    positions.update(position)
                    createdBoard.pieces.remove(enemyPiece)
                    createdBoard.updateBoard(createdBoard.pieces)
                elif validMove == True and collision == False:
                    del positions[str(sanitizedSource)]
                    position = {str(sourcePiece.location): sourcePiece.displayValue}
                    positions.update(position)
                    createdBoard.updateBoard(createdBoard.pieces)
                else:
                    print("Not a valid location for piece!")
                    continue

                #validate for presence of check
                while True:
                    if underCheck == None:
                        check = createdBoard.check(createdBoard.pieces, currentPlayer)

                    if check[0] == "check" and underCheck == None:
                        underCheck = check[1]
                        #if currentPlayer.side != underCheck:
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
                                    del positions[str(sourcePiece.location)]
                                    position = {str(sanitizedSource): sourcePiece.displayValue}
                                    positions.update(position)
                                createdBoard.updateBoard(createdBoard.pieces)
                            elif check[0] != "check":
                                turn += 1
                                underCheck = None
                        break
                    else:
                        turn += 1
                        underCheck = None
                        break
                #print(positions)
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
wk = King("w", [4, 7], "wk", 99999, False, True, 1)
wb2 = Bishop("w", [5, 7], "wb", 3, False, True, 7)
wkn2 = Knight("w", [6, 7], "wn", 3, False, False, 0)
wr2 = Rook("w", [7, 7], "wr", 5, True, False, 7)

br = Rook("b", [0, 0], "br", 5, True, False, 7)
bkn = Knight("b", [1, 0], "bn", 3, False, False, 0)
bb = Bishop("b", [2, 0], "bb", 3, False, True, 7)
bq = Queen("b", [3, 0], "bq", 9, True, True, 7)
bk = King("b", [4, 0], "bk", 99999, False, True, 1)
bb2 = Bishop("b", [5, 0], "bb", 3, False, True, 7)
bkn2 = Knight("b", [6, 0], "bn", 3, False, False, 0)
br2 = Rook("b", [7, 0], "br", 5, True, False, 7)

player1 = Player1("player1111","w", 0)
player2 = Player2("player2222","b", 0)
global positions
positions = {}
createdBoard = Chess_Board([bp1, wp1, bp2, wp2, bp3, wp3, bp4, wp4, bp5, wp5, bp6, wp6, bp7, wp7, bp8, wp8, br, wr, bkn, wkn, bb, wb, bq, wq, bk, wk, bb2, wb2, bkn2, wkn2, br2, wr2])

Game(createdBoard, player1, player2)