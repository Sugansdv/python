from translator.morse_dict import MORSE_CODE_DICT
import winsound

class MorseTranslator:
    def __init__(self):
        self.results = []

    def to_morse(self, text):
        morse = []
        for char in text.upper():
            if char in MORSE_CODE_DICT:
                morse.append(MORSE_CODE_DICT[char])
            else:
                raise ValueError(f"Unsupported character: {char}")
        return ' '.join(morse)

    def play_morse(self, morse_code):
        for symbol in morse_code:
            if symbol == '.':
                winsound.Beep(800, 100)
            elif symbol == '-':
                winsound.Beep(800, 300)
            elif symbol == ' ':
                winsound.Beep(37, 100)
            elif symbol == '/':
                winsound.Beep(37, 300)