# 7. Quiz Application
# Description: Store quiz questions and answers.
# Requirements:
# - Structure: {question: {"options": [...], "answer": ...}}
# - Loop through and accept user answers
# - Show result summary with score
# - Use nested dictionary and in check for validity
# - Track correct vs wrong answers using comprehension

quiz = {
    "What is the capital of France?": {
        "options": ["A) Berlin", "B) Paris", "C) Madrid", "D) Rome"],
        "answer": "B"
    },
    "Which language is used for web apps?": {
        "options": ["A) Python", "B) Java", "C) JavaScript", "D) C++"],
        "answer": "C"
    },
    "Who wrote 'Hamlet'?": {
        "options": ["A) Dickens", "B) Shakespeare", "C) Austen", "D) Orwell"],
        "answer": "B"
    }
}

user_answers = {}
print("Quiz Start:\n")

for question, data in quiz.items():
    print(question)
    for option in data["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer in ['A', 'B', 'C', 'D']:
        user_answers[question] = answer
    else:
        print("Invalid option. Skipped.")
        user_answers[question] = None
    print()

correct_answers = {q: a for q, a in user_answers.items() if a == quiz[q]["answer"]}
wrong_answers = {q: a for q, a in user_answers.items() if a != quiz[q]["answer"]}

print("Quiz Summary:\n")
print(f"Total Questions: {len(quiz)}")
print(f"Correct Answers: {len(correct_answers)}")
print(f"Wrong/Skipped Answers: {len(wrong_answers)}")

print("\nDetails:")
for q, ans in correct_answers.items():
    print(f" {q} → Your Answer: {ans}, Correct: {quiz[q]['answer']}")
for q, ans in wrong_answers.items():
    print(f" {q} → Your Answer: {ans}, Correct: {quiz[q]['answer']}")
