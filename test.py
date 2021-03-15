#!/usr/bin/env python3

class Piece():
    #initalize piece
    def __init__(self, location, displayValue):
        self.location = location
        self.displayValue = displayValue

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
        self.distance = distance
        self.firstMoveUsed = False

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
        valid = False
        if int(targetLocation[1]) == int(self.location[1]) + 7 or int(targetLocation[1]) == int(self.location[1]) - 7: 
                valid = True
        elif int(targetLocation[0]) == int(self.location[0]) + 7 or int(targetLocation[0]) == int(self.location[0]) - 7:
                valid = True
        else:
            valid = False
        
        if valid == True:
            self.location[0] = int(targetLocation[0])
            self.location[1] = int(targetLocation[1])
            return True
        else:
            return False
diag = [ [1, 1], [-1, 1], [1, -1], [-1, -1] ]
perpendicular = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
wp1 = Pawn("w", [0, 6], "wp", 1, True, True, 1)
wr = Rook("w", [0, 7], "wr", 5, True, False, 7)
wkn = Knight("w", [1, 7], "wn", 3, False, False, 0)
pieces = [wp1, wr, wkn]
#destination = [0, 4]
destination = [4, 7]
sourcePiece = wr

#calculate displacement
displacement = []
displacement.append(sourcePiece.location[0] - destination[0])
displacement.append(sourcePiece.location[1] - destination[1])

#x Axis
if displacement[0] != 0:
    for step in (range(abs(int(displacement[0])))):
        for piece in pieces:
            #print(sourcePiece.location[1])
            #print(piece.location[1])
            if (int(sourcePiece.location[1]) == int(piece.location[1]) and int(sourcePiece.location[0] + step) == int(piece.location[0]) and sourcePiece != piece) \
            or (int(sourcePiece.location[1]) == int(piece.location[1]) and int(sourcePiece.location[0] - step) == int(piece.location[0]) and sourcePiece != piece):
                return True
            else:
                return False
            
#y Axis
elif displacement[1] != 0:
    for step in (range(abs(int(displacement[1])))):
        for piece in pieces:
            if (int(sourcePiece.location[0])  == int(piece.location[0]) and int(sourcePiece.location[1] + step) == int(piece.location[1]) and sourcePiece != piece) \
            or (int(sourcePiece.location[0])  == int(piece.location[0]) and int(sourcePiece.location[1] - step) == int(piece.location[1]) and sourcePiece != piece)    :
                return True
            else:
                return False



# for x,y in perpendicular:
#     for step in (range(int(sourcePiece.location[1] - destination[1]))):
#         for piece in pieces:
#             #print(piece)
#             print(int(x + step))
#             #print(int(y + step))
#             if int(sourcePiece.location[0] + x + step) == int(piece.location[0]) and int(sourcePiece.location[1] + y + step) == int(piece.location[1]):
#                 print(piece.displayValue)