#  8. Number Guessing Game
# Objective: Guess a secret number.

import random
secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 5

# • Use while loop to ask for guesses.
while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}/5 - Guess the number (1 to 10): "))

        # • Use if to check guess.
        if guess == secret_number:
            print(" Correct! You guessed the number.")
            # • Use break if correct.
            break
        else:
            print(" Wrong guess. Try again.")
        attempts += 1
    except ValueError:
        print(" Please enter a valid number.")

# • Use else block if guess was never correct in 5 tries.
else:
    print(f" Out of attempts! The correct number was: {secret_number}")
