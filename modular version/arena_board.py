import colorama
import itertools
import sys

import numpy as np
from print_messages import print_life_lost, print_game_over

from random import seed,randint

class Arena_Board:
    def __init__(self, paddle):
        self.game_width = 50
        self.game_height = 50
        self.brick_width = 3
        self.frame_width = 50
        self.frame_height = 50
        self.offset = 0
        self.frame_speed = 1
        self.paddle = paddle
        self.game_clock = 0

        self.game_board = np.zeros((self.game_width, self.game_height))
    
        # self.ground_size = 1
        # self.sky_size = 1

        for __ in range(self.game_width):
            self.game_board[0][__] = 9        
            self.game_board[-1][__] = 9
        for i in range(self.paddle.X_POSITION, self.paddle.X_POSITION + self.paddle.body_width):
            self.game_board[-2][i] = 1

        number_of_bricks = randint(25, 75)

        # for i in range(number_of_bricks): randomised brick generation


    def update_clock(self):
        self.game_clock += 1
        self.display_board()

    def check_ball_collision(self):
        return 

    def restrict_paddle_movement(self):
        return

    def remove_paddle(self):
        for _ in range(self.game_width):
            if self.game_board[-2][_] == 1:
                self.game_board[-2][_] = 0
    
    def rerender_paddle(self):
        for i in range(self.paddle.X_POSITION, self.paddle.X_POSITION + self.paddle.body_width):
            self.game_board[-2][i] = 1


    def display_board(self):
        for _ in range(self.game_height):
            for __ in range(self.game_width):
                if self.game_board[_][__] == 9:
                    print("*",end="")
                elif self.game_board[_][__] == 0:
                    print(" ",end="")
                elif self.game_board[_][__] == 1:
                    print("~",end="")
                elif self.game_board[_][__] == 2:
                    print("o",end="")
                elif self.game_board[_][__] == 3:
                    print("z", end="")
            print()
        print(self.paddle.X_POSITION)