def validate_input(func):
    def wrapper(self, letter):
        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input. Please enter a single alphabet letter.")
            return False
        return func(self, letter.lower())
    return wrapper
