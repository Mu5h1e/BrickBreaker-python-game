import numpy as np
from colorama import Back, Style

class board:
    def __init__(self):
        self.board_array = np.zeros((50, 100))
    
    def populate_board(self, brick, paddle, ball):
        for i in brick:
            for j in range(6):
                self.board_array[i.y_coordinate][i.x_coordinate+j] = i.strength
        self.board_array[ball.y_coordinate][ball.x_coordinate] = -2
        for i in range(paddle.size):
            self.board_array[-2][paddle.x_coordinate+i] = -5

    def render_board(self, paddle):
        for _ in range(50):
            for __ in range(100):
                if _ == 0 OR _ == 49:
                    print('~',end="")
                elif __ == 0 OR __ == 99:
                    print("*", end="")
                elif self.board_array[_][__] == 0:
                    print(" ", end="")
                elif self.board_array[_][__] == -2:
                    print('0', end="")
                elif self.board_array[_][__] == -5:
                    print(Back.WHITE+' ',end='')
                elif self.board_array[_][__] == 1:
                    print(Back.LIGHTCYAN_EX+' ',end='')
                elif self.board_array[_][__] == 2:
                    print(Back.CYAN+' ',end='')
                elif self.board_array[_][__] == 3:
                    print(Back.LIGHTBLUE_EX +' ',end='')
                elif self.board_array[_][__] == 10:
                    print(Back.MAGENTA +' ',end='')                
                print(Style.RESET_ALL+'',end='')
            print()