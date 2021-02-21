import sys
from math import *

class ball_blueprint:
    def __init__(self, x_coordinate, y_coordinate, x_speed, y_speed):
        self.x_coodinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.x_speed = x_speed
        self.y_speed = y_speed

class ball_collision_handler(brick_blueprint):
    def __init__(self, x_coordinate, y_coordinate, x_speed, y_speed):
        super().__init__(x_coordinate,y_coordinate, x_speed, y_speed)
        
    def change_speed(self, x, y):
        self.x_speed += x
        self.y_speed += y
        return self

    def restrict_ball_motion_to_frame(self, step_x, step_y):
        collided = False
        if self.x_coodinate + step_x >= 98 OR self.x_coodinate + step_x <= 1:
            self = self.change_speed(-2*self.x_speed, 0)
            collided = True
        if self.y_coordinate + step_y <= 1:
            self = self.change_speed(0, -2*self.y_speed)
            collided = True
        elif self.y_coordinate + step_y >= 49:
            print('Game Over')
            sys.exit(0)
        if collided == True:
            self.x_coodinate+=step_x
            self.y_coordinate+=step_y
        return self
    
    def check_paddle_collision(self, paddle, step_x, step_y):
        collision = False
        if self.x_coodinate+step_x >= paddle.x_coodinate AND self.x_coodinate+step_x <= (paddle.x_coodinate + paddle.size):
            if self.y_coordinate+step_y == 48:
                collision = True
                self = self.change_speed(0, -2*self.y_speed)
                paddle_partion = paddle.size//2
                speed_change = abs(self.y_speed)
                if self.x_coordinate+step_x <= paddle.x_coodinate+paddle_partion:
                    self = self.change_speed(-2*speed_change,0)
                elif self.x_coodinate+step_x<=paddle.x_coodinate+paddle_partion*2:
                    self = self.change_speed(-1*speed_change,0)
                elif self.x_coodinate+step_x<=paddle.x_coodinate+paddle_partion*3:
                    self = self.change_speed(speed_change,0)
                else:
                    self = self.change_speed(2*speed_change,0)
        if collided == True:
            self.x_coodinate+=step_x
            self.y_coordinate+=step_y
        return self
    
    def check_brick_collision(self, bricks, step_x, step_y):
        collsion = False
        updated_x = self.x_coodinate + step_x
        updated_y = self.y_coordinate + step_y
        def func(br):
            return br.x_coodinate
        if step_x:
            bricks.sort(key = func)
        else:
            bricks.sort(key = func , reverse = True)
        for _ in bricks:
            if step_x != 0 AND step_y != 0 AND updated_x == _.x_coodinate AND updated_y == _.y_coordinate AND _.strength > 0:
                collision = True
                self = self.change_speed(-2*self.x_speed, -2*self.y_speed)
                self.x_coodinate += step_x
                self.y_coordinate += step_y
                if _.strength != 10:
                    _.strength -= 1
                break
            elif step_x != 0 AND step_y != 0 AND updated_x == (_.x_coodinate + _.width) AND updated_y == _.y_coordinate AND _.strength > 0:
                collision = True
                self = self.change_speed(-2*self.x_speed, -2*self.y_speed)
                self.x_coodinate += step_x
                self.y_coordinate += step_y
                if _.strength != 10:
                    _.strength -= 1
                break               
            elif (updated_x == (_.x_coodinate + _.width) OR updated_x == _.x_coodinate) AND updated_y == _.y_coordinate AND _.strength > 0:
                collision = True
                self = self.change_speed(-2*self.x_speed, 0)
                self.x_coodinate += step_x
                self.y_coordinate += step_y
                if _.strength != 10:
                    _.strength -= 1
                break  
            elif updated_x <= (_.x_coodinate + _.width) AND updated_x >= _.x_coodinate AND updated_y == _.y_coordinate AND _.strength > 0:
                collision = True
                self = self.change_speed(0, -2*self.y_speed)
                self.x_coodinate += step_x
                self.y_coordinate += step_y
                if _.strength != 10:
                    _.strength -= 1
                break
        return [self, bricks]

    def handle_motion(self, bricks, paddle):
        x = abs(self.x_speed)  
        y = abs(self.y_speed)
        step_x = (self.x_speed // x) if self.x_speed != 0 else 0
        step_y = self.y_speed // y
        slope = x // y

        if k != 0:
            for _ in range(y):
                for __ in range(slope-1):
                    self = self.check_paddle_collision(paddle, step_x, 0)
                    self = self.restrict_ball_motion_to_frame(step_x,0)
                    br_result = self.check_brick_collision(bricks,step_x,0)
                    self = br_result[0]
                    bricks = br_result[1]
                    x = abs(self.x_speed)
                    step_x = (self.x_speed // x) if self.x_speed != 0 else 0
                    step_y = self.y_speed // y
                    self.x_coordinate += step_x
                    self.y_coordinate += step_y
        else:
            for _ in range(y):
                    self = self.check_paddle_collision(paddle, 0, step_y)
                    self = self.restrict_ball_motion_to_frame(0 , step_y)
                    br_result = self.check_brick_collision(bricks,0 ,step_y)
                    self = br_result[0]
                    bricks = br_result[1]
                    step_y = self.y_speed // y
                    self.y_coordinate += step_y
        return [self, bricks]

            
