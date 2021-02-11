def paddle_handler(board, paddle, char):
    
    if char == 'a':
        can_move = board.check(paddle, char)
        if can_move:
            board.remove_paddle(paddle)
            paddle.move_left()
            board.move_paddle(paddle)
    
    if char == 'd':
        can_move = board.check(paddle, char)
        if can_move:
            board.remove_paddle(paddle)
            paddle.move_right()
            board.move_paddle(paddle)