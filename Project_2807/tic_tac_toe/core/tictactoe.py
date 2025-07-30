import random
from core.decorators import validate_move

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        print("\n")
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def is_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def get_empty_cells(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    yield (i, j)

    @validate_move
    def make_move(self, row, col):
        self.board[row][col] = self.current_player

    def ai_move(self):
        empty_cells = list(self.get_empty_cells())
        if empty_cells:
            return random.choice(empty_cells)
        return None

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        self.display_board()

        while True:
            if self.current_player == "X":
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter col (0-2): "))
                    self.make_move(row, col)
                except Exception as e:
                    print(f"Error: {e}")
                    continue
            else:
                print("AI is making a move...")
                row, col = self.ai_move()
                self.make_move(row, col)

            self.display_board()

            if self.is_winner(self.current_player):
                print(f"Player {self.current_player} wins!")
                break
            if self.is_draw():
                print("It's a draw!")
                break

            self.switch_player()
