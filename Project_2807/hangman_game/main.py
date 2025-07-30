from core.hangman import Hangman
from core.decorators import validate_input

class Game:
    def __init__(self):
        self.hangman = Hangman()
        self.hint_generator = self.hangman.generate_hint()

    @validate_input
    def guess_letter(self, letter):
        if letter in self.hangman.guessed_letters:
            print(" You've already guessed that letter.")
            return False

        self.hangman.guessed_letters.append(letter)

        if letter in self.hangman.word:
            print(" Correct!")
        else:
            print(" Incorrect.")
            self.hangman.attempts -= 1
            self.hangman.failed_attempts += 1

            if self.hangman.failed_attempts == 3 and not self.hangman.used_hints:
                self.hangman.used_hints = True
                try:
                    hint = next(self.hint_generator)
                    print(f" Hint: The word contains the letter '{hint}'")
                except StopIteration:
                    print("No hints available.")
        return True

    def start(self):
        print(" Welcome to Hangman!")
        while not self.hangman.is_game_over():
            print("\n" + self.hangman.display_word())
            self.hangman.show_hangman_state(self.hangman.attempts)
            guess = input("Enter your guess (a-z): ")
            self.guess_letter(guess)

        print("\n Game Over!")
        if "_" not in self.hangman.display_word():
            print(" You guessed the word:", self.hangman.word)
        else:
            print(" You lost. The word was:", self.hangman.word)

if __name__ == "__main__":
    game = Game()
    game.start()
