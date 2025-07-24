import random

class GameOverError(Exception):
    pass

number = random.randint(1, 10)
attempts = 0

while attempts < 5:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed it.")
            break
        else:
            print("Wrong guess.")
    except ValueError:
        print("Please enter a valid number.")
    finally:
        print(f"Attempts used: {attempts}/5")

    if attempts == 5:
        raise GameOverError("Game Over! You've used all 5 attempts.")
