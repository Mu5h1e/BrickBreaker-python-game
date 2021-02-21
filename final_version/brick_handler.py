import numpy as np

class brick_blueprint:
    def __init__(self, x_coordinate, y_coordinate):
        self.width = 6
        self.height = 1
        self.x_coordinate = x
        self.y_coordinate = y

class strength_1(brick_blueprint):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__(x_coordinate,y_coordinate)
        self.strength = 1
        self.instant = False

class strength_2(brick_blueprint):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__(x_coordinate,y_coordinate)
        self.strength = 2
        self.instant = False
        
class strength_3(brick_blueprint):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__(x_coordinate, y_coordinate)
        self.strength = 3
        self.instant = False

class unbreakable(brick_blueprint):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__(x_coordinate,y__coordinate)
        self.strength = 10
        self.instant = False
