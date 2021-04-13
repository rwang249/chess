from piece import Piece

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
    def move(self, targetLocation, validateCheckmate):
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
            if validateCheckmate == True:
                return [True, targetLocation]
            else:
                self.location[0] = int(targetLocation[0])
                self.location[1] = int(targetLocation[1])
                return [True, targetLocation]
        else:
            return [False, targetLocation]
