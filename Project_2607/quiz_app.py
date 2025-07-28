import json
import random
import time
import os

QUESTION_FILE = 'question_bank.json'


# ---------------------------
# Load or initialize question bank
# ---------------------------
def load_questions():
    if os.path.exists(QUESTION_FILE):
        with open(QUESTION_FILE, 'r') as file:
            return json.load(file)
    return []


def save_questions(questions):
    with open(QUESTION_FILE, 'w') as file:
        json.dump(questions, file, indent=2)


# ---------------------------
# Add new question
# ---------------------------
def add_question():
    print("\n--- Add a New Question ---")
    q_type = input("Type (mcq/truefalse): ").strip().lower()
    difficulty = input("Difficulty (easy/medium/hard): ").strip().lower()
    question = input("Enter the question: ")

    if q_type == 'mcq':
        options = []
        for i in range(4):
            opt = input(f"Option {i + 1}: ")
            options.append(opt)
        correct = input("Correct option number (1-4): ")
        correct_answer = options[int(correct) - 1]
    elif q_type == 'truefalse':
        correct_answer = input("Answer (True/False): ").capitalize()
        options = ["True", "False"]
    else:
        print("Invalid type.")
        return

    new_q = {
        "type": q_type,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "answer": correct_answer
    }

    questions = load_questions()
    questions.append(new_q)
    save_questions(questions)
    print("Question added!")


# ---------------------------
# Run the quiz
# ---------------------------
def run_quiz():
    questions = load_questions()
    if not questions:
        print("No questions available. Add some first.")
        return

    difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
    filtered = [q for q in questions if q['difficulty'] == difficulty]

    if not filtered:
        print(f"No questions available for '{difficulty}'.")
        return

    random.shuffle(filtered)
    score = 0
    total = len(filtered)

    print(f"\n--- Starting {difficulty.capitalize()} Quiz ({total} questions) ---\n")

    for i, q in enumerate(filtered, 1):
        print(f"Q{i}: {q['question']}")
        for idx, opt in enumerate(q['options'], 1):
            print(f"  {idx}. {opt}")
        
        start_time = time.time()
        try:
            answer = input("Your answer (number or text): ").strip()
            elapsed = time.time() - start_time

            if elapsed > 20:
                print(" Time's up! Skipping question.")
                continue

            user_ans = q['options'][int(answer) - 1] if answer.isdigit() else answer
            if user_ans.lower() == q['answer'].lower():
                print(" Correct!\n")
                score += 1
            else:
                print(f" Wrong! Correct: {q['answer']}\n")
        except Exception:
            print(" Invalid input. Skipping.\n")

    print(f" Quiz Completed! Score: {score}/{total}\n")


# ---------------------------
# Main Menu
# ---------------------------
def main():
    while True:
        print("=====  Quiz Application =====")
        print("1. Start Quiz")
        print("2. Add Question")
        print("3. View All Questions")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            run_quiz()
        elif choice == '2':
            add_question()
        elif choice == '3':
            questions = load_questions()
            for i, q in enumerate(questions, 1):
                print(f"{i}. [{q['difficulty']}] {q['question']} ({q['type']})")
        elif choice == '4':
            print("Exiting Quiz App.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
