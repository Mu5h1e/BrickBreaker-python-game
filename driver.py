import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)


class display_controller:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.timer = 0
        self.display_matrix = np.zeros((self.width, self.height))
    
    def display_timer(self):
        return self.timer
    
    def init_matrix(self):
        self.display_matrix[self.height-1][((self.width//2)-3):((self.width//2)+2)] = 1
    
    def refreshed_matrix(self):
        for _ in range(self.height):
            for __ in range(self.width):
                print({True: " ", False: "1"}[self.display_matrix[_][__] == 0], end=" ")
            print()


class paddle_controller:
    def __init__ (self, position, input_key):
        self.position = position
        self.input = input_key

    def handle_a_key(self):
        self.position -= 1
    
    def handle_d_key(self):
        self.position += 1
    
    def get_position(self):
        return self.postion


def driver_function():
    dc = display_controller()
    dc.init_matrix()
    dc.refreshed_matrix()

if __name__ == '__main__':
    driver_function()