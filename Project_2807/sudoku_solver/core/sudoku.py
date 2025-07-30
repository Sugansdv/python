import csv
from core.decorators import timeit

class InvalidGridError(Exception):
    pass

class Sudoku:
    def __init__(self, filepath):
        self.grid = self.load_puzzle(filepath)

    def load_puzzle(self, filepath):
        grid = []
        try:
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    grid.append([int(num) for num in row])
        except Exception as e:
            raise InvalidGridError("Invalid CSV or grid data.") from e

        if len(grid) != 9 or any(len(row) != 9 for row in grid):
            raise InvalidGridError("Grid must be 9x9.")

        return grid

    def display(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else "." for num in row))

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if self.grid[box_row+i][box_col+j] == num:
                    return False
        return True

    def possible_numbers(self, row, col):
        return (num for num in range(1, 10) if self.is_valid(row, col, num))

    @timeit
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in self.possible_numbers(row, col):
                        self.grid[row][col] = num
                        if self.solve():
                            return True
                        self.grid[row][col] = 0
                    return False
        return True
