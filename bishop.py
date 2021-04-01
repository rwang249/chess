from piece import Piece

class Bishop(Piece):
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
        diagonal = [(1,1),(-1,1),(1,-1),(-1,-1)]
        
        #diagonal
        for x, y in diagonal:
            for step in range(1, 7):
                if int(targetLocation[0]) == int(self.location[0]) + int(x * step) and int(targetLocation[1]) == int(self.location[1]) + int(y * step):
                    self.location[0] = int(targetLocation[0])
                    self.location[1] = int(targetLocation[1])
                    return True
        return False