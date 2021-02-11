import colorama
import itertools
import sys

import numpy as np
from print_messages import print_life_lost, print_game_over

from component_creation import boxstable
from random import seed,randint

class Arena_Board:
    def __init__(self, paddle):
        self.game_width = 50
        self.game_height = 52
        
        self.frame_width = 50
        self.frame_height = 50
        self.offset = 0
        self.frame_speed = 1

        self.game_clock = 0

        self.game_board = np.zeros((self.game_width, self.game_height))
    
        # self.ground_size = 1
        # self.sky_size = 1

        for __ in range(self.game_width):
            self.gameBoardArr[0][__] = 9        
            self.gameBoardArr[-1][__] = 9
        
        for i in range(paddle.X_POSITION, paddle.X_POSITION + paddle.body_width):
            self.gameBoardArr[-2][i] = 1
    
    def update_clock(self):
        self.gameClock += 1