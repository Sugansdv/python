import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from test.core import TypingTest
from utils.helpers import word_generator

SAMPLES_PATH = "data/samples.txt"
SCORE_FILE = "scores/high_scores.txt"

def load_samples():
    with open(SAMPLES_PATH, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_scores(results):
    os.makedirs("scores", exist_ok=True)
    with open(SCORE_FILE, "a") as f:
        for speed, accuracy in results:
            f.write(f"{speed} WPM, {accuracy}% accuracy\n")

def main():
    samples = load_samples()
    gen = word_generator(samples)
    test = TypingTest(samples)

    while True:
        sample = next(gen)
        speed, accuracy = test.run_test(sample)
        print(f"\nYour Speed: {speed} WPM")
        print(f"Accuracy: {accuracy}%")

        again = input("\nTry again? (y/n): ")
        if again.lower() != 'y':
            break

    save_scores(test.results)
    print("\nScores saved. Goodbye!")

if __name__ == "__main__":
    main()
