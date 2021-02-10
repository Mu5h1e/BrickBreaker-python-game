import numpy as np

class display_controller:
    def __init__(self):
        self.width = 100
        self.height = 100
        self.timer = 0
        self.display_matrix = np.zeros((100,100))
    
    def display_timer(self):
        return self.timer
    
    def print_matrix(self):
        print(self.display_matrix)

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
    dc1 = display_controller()
    dc1.print_matrix()

if __name__ == '__main__':
    driver_function()