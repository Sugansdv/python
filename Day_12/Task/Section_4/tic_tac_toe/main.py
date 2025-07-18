from player import get_move
from board import display
from game import check_win

board = [' '] * 9
current = 'X'

for _ in range(9):
    display(board)
    pos = get_move()
    if board[pos - 1] == ' ':
        board[pos - 1] = current
        if check_win(board, current):
            display(board)
            print(f"Player {current} wins!")
            break
        current = 'O' if current == 'X' else 'X'
    else:
        print("Position already taken.")
else:
    print("It's a draw!")
