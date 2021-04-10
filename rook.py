from piece import Piece

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
    def move(self, targetLocation, validateCheckmate):
        if int(targetLocation[0]) <= 7 and int(targetLocation[1]) == self.location[1]:
            if validateCheckmate == True:
                return True, targetLocation
            else:
                self.location[0] = int(targetLocation[0])
                self.location[1] = int(targetLocation[1])
                return True
        elif int(targetLocation[1]) <= 7 and int(targetLocation[0]) == self.location[0]: 
            if validateCheckmate == True:
                return True, targetLocation
            else:
                self.location[0] = int(targetLocation[0])
                self.location[1] = int(targetLocation[1])
                return True
        else:
            return False