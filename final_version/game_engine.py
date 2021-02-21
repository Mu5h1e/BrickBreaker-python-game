import numpy as np 
from random import randint, seed

class game_engine:
    def __init__(self):
        seed(np.random.rand())
        self.brick_arr = []