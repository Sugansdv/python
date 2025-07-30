import time

class TypingTest:
    def __init__(self, samples):
        self.samples = samples
        self.results = []

    def run_test(self, sample):
        print("\nType this sentence:")
        print(f"\n{sample}\n")
        input("Press Enter when ready...")

        start = time.time()
        typed = input("\nStart typing: ")
        end = time.time()

        duration = end - start
        words = len(typed.split())
        speed = round((words / duration) * 60, 2) if duration > 0 else 0

        correct = sum(1 for a, b in zip(typed, sample) if a == b)
        accuracy = round((correct / len(sample)) * 100, 2) if sample else 0

        self.results.append((speed, accuracy))
        return speed, accuracy
