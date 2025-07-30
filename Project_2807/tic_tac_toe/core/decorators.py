def validate_move(func):
    def wrapper(self, row, col):
        if not (0 <= row <= 2 and 0 <= col <= 2):
            raise ValueError("Position out of bounds.")
        if self.board[row][col] != " ":
            raise ValueError("Cell already taken.")
        return func(self, row, col)
    return wrapper
