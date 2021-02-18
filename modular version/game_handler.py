def paddle_handler(board, paddle, char):
    
    if char == 'a':
            board.remove_paddle()
            paddle.move_left()
            board.rerender_paddle()
            board.display_board()
    
    if char == 'd':
            board.remove_paddle()
            paddle.move_right()
            board.rerender_paddle()
            board.display_board()