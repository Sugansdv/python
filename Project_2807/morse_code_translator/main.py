from translator.core import MorseTranslator
from utils.helpers import morse_generator
import os

TRANSLATION_FILE = "data/translations.txt"

def save_translation(text, morse):
    os.makedirs("data", exist_ok=True)
    with open(TRANSLATION_FILE, "a") as f:
        f.write(f"{text} => {morse}\n")

def main():
    translator = MorseTranslator()

    while True:
        text = input("\nEnter text to translate to Morse Code: ").strip()
        try:
            morse = translator.to_morse(text)
            print("Morse Code:", morse)

            print("Playing Morse code...")
            translator.play_morse(morse)

            save_translation(text, morse)

            print("Saved translation.")
        except ValueError as e:
            print("Error:", e)

        again = input("Translate another? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()