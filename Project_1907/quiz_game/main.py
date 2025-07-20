from quiz.quiz_engine import run_quiz
from quiz.question_bank.questions import get_questions

def main():
    print(" Welcome to the Python Quiz Game!")
    questions = get_questions()
    run_quiz(questions)

if __name__ == "__main__":
    main()
