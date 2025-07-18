from questions import get_questions
from evaluate import evaluate_answers
from user import get_username

def main():
    user = get_username()
    print(f"\nWelcome, {user}!\n")
    questions = get_questions()
    responses = []

    for q in questions:
        ans = input(q["question"] + " ")
        responses.append(ans)

    score = evaluate_answers(questions, responses)
    print(f"\nYour score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
