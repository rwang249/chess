from piece import Piece

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

