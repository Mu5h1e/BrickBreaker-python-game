
class item:
    def __init__(self):
        self.X_POSITION = 10
        self.Y_POSITION = 0
        self.LIVES = 3

class paddleBoi(item):
    def __init__(self):
        super().__init__()
        self.body = ['~','~','~','~','~']
        self.body_width = 5
        self.LIVES = 3
        self.SCORE = 0
        self.speed = 1
    
    def move_left(self):
        self.X_POSITION = self.X_POSITION - 1
    
    def move_right(self):
        self.X_POSITION = self.X_POSITION + 1
    
    def display(self):
        for i in self.body:
            print(i, end='')