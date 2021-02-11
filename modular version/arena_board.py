import colorama
import itertools
import sys

from print_messages import print_life_lost, print_game_over

from component_creation import boxstable
from random import seed,randint

class Arena_Board:
    def __init__(self, paddle):
        self.game_width = 50
        self.game_height = 50
        
        self.frame_width = 50
        self.frame_height = 50
        self.offset = 0
        self.frame_speed = 1

        self.game_clock = 0

        self.gameBoardArr = [[[" "] for i in range(self.gameWidth)] for j in range(self.gameHeight)]
    
        self.ground_size = 1
        self.sky_size = 1

        for i in range(self.sky_size):
            for aj in range(self.game_width):
                self.gameBoardArr[i][j][0] = "*"
        
        for i in range(self.ground_size):
            for j in range(self.game_width):
                self.gameBoardArr[i][j][0] = "*"
        
        for i in range(paddle.X_POSITION, paddle.X_POSITION + paddle.body_width):
            self.gameBoardArr[-self.ground_size -1][j][0] = "~"
    
    def update_clock(self):
        self.gameClock += 1