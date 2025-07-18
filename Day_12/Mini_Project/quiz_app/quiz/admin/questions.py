import json
import os

QUESTIONS_FILE = "quiz/questions.json"

def add_question(question, options, answer):
    if not os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, 'w') as f:
            json.dump([], f)

    with open(QUESTIONS_FILE, 'r') as f:
        data = json.load(f)

    data.append({
        "question": question,
        "options": options,
        "answer": answer
    })

    with open(QUESTIONS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def view_questions():
    if not os.path.exists(QUESTIONS_FILE):
        print("No questions found.")
        return

    with open(QUESTIONS_FILE, 'r') as f:
        data = json.load(f)

    for idx, q in enumerate(data, 1):
        print(f"\nQ{idx}: {q['question']}")
        for i, opt in enumerate(q['options'], 1):
            print(f"   {i}. {opt}")
