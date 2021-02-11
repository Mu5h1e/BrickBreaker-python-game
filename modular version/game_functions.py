import os
import input

from game_handler import paddle_handler
from arena_board import Arena_Board
from component_creation import paddleBoi
from print_messages import print_game_over

def end_game():
    print_game_over()
    return 1

def game_loop(arena, paddle):

    if paddle.LIVES <= 0:
        game_end = end_game()
    else:
        arena.update_clock()
        arena.print_arena(paddle)
        arena.update_frame(paddle)
        game_end=0
    
    return end_game

def start_game():
    
    paddle=paddleBoi()
    arena_instance=Arena_Board(paddleBoi)
    os.system('clear')

    while True:
        gameEnd = game_loop(arena_instance, paddle)
        char = input.get()
        
        if char == 'q':
            gameEnd += end_game()
        else: 
            paddle_handler(arena_instance, paddle, char)
        
        if gameEnd == 1:
            break