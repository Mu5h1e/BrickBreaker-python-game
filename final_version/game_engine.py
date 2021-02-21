import numpy as np 
from brick_handler import *
from paddle_handler import paddle_handler
from random import randint, seed

class game_engine:
    def __init__(self):
        self.brick_generator()
        self.paddle_generator()
        
    def brick_generator(self):
        seed(np.random.rand())
        self.brick_arr = []
        top_end = 15
        bottom_end = 20
        left_end = 23
        right_end = 77
        for _ in range(top_end, bottom_end):
            for __ in range(left_end,right_end,6):
                selector = randint(1,5)
                if selector == 1:
                    brick = strength_1(__,_)
                    self.brick_arr.append(brick)
                if selector == 2:
                    brick = strength_2(__,_)
                    self.brick_arr.append(brick)    
                if selector == 3:
                    brick = strength_3(__,_)
                    self.brick_arr.append(brick)   
                else:
                    brick = unbreakable(__,_)
                    self.brick_arr.append(brick)         
    
    def paddle_generator(self):
        self.paddle = paddle_handler(47)