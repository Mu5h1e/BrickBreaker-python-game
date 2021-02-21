class paddle_handler:
    def __init__(self, x_coordinate):
        self.width = 5
        self.x_coordinate = x_coordinate
        self.LIVES = 3
        self.speed = 1
    
    def move(self, inp):
        x = self.x_coordinate
        if inp == 'a':
            x -= self.speed
        elif inp == 'd':
            x += self.speed
        if x <= 0:
            x = 0
        if x >= 100:
            x=100
