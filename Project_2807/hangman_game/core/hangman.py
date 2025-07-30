import random

class Hangman:
    def __init__(self, word_list_file="data/words.txt"):
        self.word = self.load_word(word_list_file)
        self.attempts = 6
        self.failed_attempts = 0
        self.guessed_letters = []
        self.used_hints = False

    def load_word(self, filepath):
        try:
            with open(filepath, "r") as file:
                words = [line.strip() for line in file if line.strip()]
                return random.choice(words).lower()
        except FileNotFoundError:
            print("Word list file not found.")
            return "python"

    def display_word(self):
        return " ".join([char if char in self.guessed_letters else "_" for char in self.word])

    def is_game_over(self):
        return self.attempts == 0 or "_" not in self.display_word()

    def generate_hint(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                yield letter

    @staticmethod
    def show_hangman_state(attempts_left):
        states = [
            "😵  |----|\n     |    O\n     |   /|\\\n     |   / \\\n    _|_",
            "😰  |----|\n     |    O\n     |   /|\\\n     |   / \n    _|_",
            "😟  |----|\n     |    O\n     |   /|\\\n     |    \n    _|_",
            "😕  |----|\n     |    O\n     |   /|\n     |    \n    _|_",
            "😐  |----|\n     |    O\n     |    |\n     |    \n    _|_",
            "🙂  |----|\n     |    O\n     |    \n     |    \n    _|_",
            "😀  |----|\n     |     \n     |     \n     |     \n    _|_",
        ]
        print(states[6 - attempts_left])
