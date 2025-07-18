import json
import random
import time

def load_questions(path="quiz/questions.json"):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Questions file not found!")
        return []

def start_quiz():
    questions = load_questions()
    if not questions:
        print("No quiz questions available.")
        return 0

    score = 0
    random.shuffle(questions)
    start = time.time()

    for q in questions:
        print(f"\n{q['question']}")
        for i, opt in enumerate(q['options'], 1):
            print(f"  {i}. {opt}")

        try:
            ans = int(input("Your answer (1-4): "))
            if q['options'][ans - 1] == q['answer']:
                score += 1
        except:
            print("Invalid input. Skipping.")

    end = time.time()
    print(f"\nQuiz completed in {round(end - start, 2)} seconds.")
    return score
