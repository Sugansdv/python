from core.sudoku import Sudoku

def main():
    sudoku = Sudoku("puzzles/puzzle.csv")
    print("Initial Puzzle:")
    sudoku.display()

    if sudoku.solve():
        print("\nSolved Puzzle:")
        sudoku.display()
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
