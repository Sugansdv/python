import logging

logging.basicConfig(filename='quiz_exceptions.log', level=logging.ERROR)

class InvalidAnswerError(Exception):
    pass

questions = {
    "What is the capital of France?": "B",
    "What is 2 + 2?": "A",
    "Which is a fruit?": "C"
}

options = {
    "What is the capital of France?": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
    "What is 2 + 2?": ["A. 4", "B. 5", "C. 6", "D. 3"],
    "Which is a fruit?": ["A. Potato", "B. Onion", "C. Apple", "D. Carrot"]
}

score = 0

for q, ans in questions.items():
    try:
        print(q)
        for opt in options[q]:
            print(opt)
        user_input = input("Your answer (A/B/C/D): ").strip().upper()

        if user_input not in ['A', 'B', 'C', 'D']:
            raise InvalidAnswerError("Answer must be one of A/B/C/D.")

        if user_input == ans:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong.\n")
    except InvalidAnswerError as e:
        print(f"Invalid input: {e}")
        logging.error(f"InvalidAnswerError: {e}")
    except Exception as e:
        print("An unexpected error occurred.")
        logging.error(f"Unexpected Error: {e}")

print(f"Your score: {score}/{len(questions)}")
