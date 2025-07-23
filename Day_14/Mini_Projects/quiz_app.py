import csv
import os
from datetime import datetime

QUESTIONS_FILE = "questions.csv"
RESULTS_FILE = "results.csv"

# Load questions from CSV
def load_questions(filename):
    questions = []
    if not os.path.exists(filename):
        print(" Questions file not found.")
        return questions

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append({
                "question": row["question"],
                "options": [row["option1"], row["option2"], row["option3"], row["option4"]],
                "answer": int(row["answer"])
            })
    return questions

# Save result
def save_result(name, score, total):
    file_exists = os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Score", "Total", "Timestamp"])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([name, score, total, timestamp])

# Main quiz logic
def run_quiz():
    name = input("Enter your name: ").strip()
    questions = load_questions(QUESTIONS_FILE)

    if not questions:
        return

    score = 0
    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for i, opt in enumerate(q["options"], 1):
            print(f"  {i}. {opt}")

        try:
            user_ans = int(input("Your answer (1-4): "))
            if user_ans == q["answer"]:
                score += 1
        except ValueError:
            print(" Invalid input. Moving to next question.")

    print(f"\n{name}, your score: {score}/{len(questions)}")
    save_result(name, score, len(questions))

if __name__ == "__main__":
    run_quiz()
