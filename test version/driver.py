import numpy as np
import sys, os
import input
np.set_printoptions(threshold=sys.maxsize)

class game_engine:
    def __init__(self, timer=0, paddle_position=None, prev_ball_position=None, curr_ball_position=None, collision_point_paddle=None):
        self.timer = timer
        self.width = 50
        self.height = 50
        self.paddle_position = paddle_controller
        self.prev_ball_position = prev_ball_position
        self.curr_ball_position = curr_ball_position
        self.collision_point_paddle = collision_point_paddle
        self.display_matrix = np.zeros((self.width, self.height))
    
    def set_position(self, position):
        self.display_matrix[self.height-1][(position-3):(position+2)] = 1

    def handle_refresh(self, position):
        self.display_matrix = np.zeros((self.width, self.height))
        self.timer+=1
        self.set_position(position)
         

class display_controller:
    def __init__(self, position,height, width):
        self.timer = 0
        self.height = height
        self.width = width
        self.post_paddle_collision_slope = 1
    
    def display_refreshed_matrix(self, display_matrix):
        for _ in range(self.height):
            for __ in range(self.width):
                print({True: " ", False: "1"}[display_matrix[_][__] == 0], end=" ")
            print()


class paddle_controller:
    def __init__ (self, position):
        self.position = position

    def handle_a_key(self):
        self.position -= 1
    
    def handle_d_key(self):
        self.position += 1
    
    def get_position(self):
        return self.postion


def driver_function():
    start = False
    ge = game_engine()
    ge.set_position(25)
    dc = display_controller(5,ge.height,ge.width)
    dc.display_refreshed_matrix(ge.display_matrix)
    pc = paddle_controller(dc.width//2)
    s = input("input s to start")
    if s == "s": 
        start = True
    else:
        driver_function()

    while start:
        inp = input("enter a or d")
        os.system('clear')
        inst = inp.get()
        if inst == 'a':
            pc.handle_a_key()
            print(pc.position)
            ge.handle_refresh(pc.position)
        else:
            pc.handle_d_key()
            ge.handle_refresh(pc.position)
        dc.display_refreshed_matrix(ge.display_matrix)


if __name__ == '__main__':
    driver_function()