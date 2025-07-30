from core.evaluator import evaluate_strength
from core.feedback import missing_criteria_generator

def main():
    while True:
        password = input("Enter your password: ").strip()
        if not password:
            print("Error: Password cannot be empty.")
            continue

        strength = evaluate_strength(password)
        print(f"Strength: {strength}")

        if strength != "Strong":
            print("Suggestions:")
            for feedback in missing_criteria_generator(password):
                print("-", feedback)
        else:
            break

if __name__ == "__main__":
    main()
