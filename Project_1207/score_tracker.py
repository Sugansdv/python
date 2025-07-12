#3. Quiz Game with Score Tracking
questions = [
    {"q": "What is the capital of France?", "answer": "Paris"},
    {"q": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"q": "Who wrote 'Hamlet'?", "answer": "Shakespeare"},
    {"q": "What is 5 * 6?", "answer": "30"},
    {"q": "In which year did India gain independence?", "answer": "1947"}
]


def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.lower()

def start_quiz():
    score = 0
    index = 0

    while index < len(questions): 
        print(f"\nQ{index+1}: {questions[index]['q']}")
        user_input = input("Your answer: ")
        if check_answer(user_input, questions[index]['answer']):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {questions[index]['answer']}")
        index += 1

    print("\n--- Quiz Completed ---")
    print(f"Your Score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

start_quiz()
