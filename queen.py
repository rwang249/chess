from piece import Piece

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

    def move(self, targetLocation, validateCheckmate):
        diagonal = [(1,1),(-1,1),(1,-1),(-1,-1)]
        #perpendicular
        if int(targetLocation[0]) <= 7 and int(targetLocation[1]) == self.location[1]:
            if validateCheckmate == True:
                return [True, targetLocation]
            else:
                self.location[0] = int(targetLocation[0])
                self.location[1] = int(targetLocation[1])
                return [True, targetLocation]
        elif int(targetLocation[1]) <= 7 and int(targetLocation[0]) == self.location[0]: 
            if validateCheckmate == True:
                return [True, targetLocation]
            else:
                self.location[0] = int(targetLocation[0])
                self.location[1] = int(targetLocation[1])
                return [True, targetLocation]
        
        #diagonal
        for x, y in diagonal:
            for step in range(1, 7):
                if int(targetLocation[0]) == int(self.location[0]) + int(x * step) and int(targetLocation[1]) == int(self.location[1]) + int(y * step):
                    if validateCheckmate == True:
                        return [True, targetLocation]
                    else:
                        self.location[0] = int(targetLocation[0])
                        self.location[1] = int(targetLocation[1])
                        return [True, targetLocation]
        return [False, targetLocation]