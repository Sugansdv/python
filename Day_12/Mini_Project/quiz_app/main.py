from quiz.admin import questions
from quiz.user import evaluate
from quiz import score

def admin_mode():
    while True:
        print("\nAdmin Menu:\n1. Add Question\n2. View Questions\n3. Back")
        choice = input("Enter choice: ")
        if choice == '1':
            q = input("Enter question: ")
            opts = [input(f"Option {i+1}: ") for i in range(4)]
            ans = input("Enter correct answer: ")
            questions.add_question(q, opts, ans)
        elif choice == '2':
            questions.view_questions()
        else:
            break

def user_mode():
    name = input("Enter your name: ")
    print("\nStarting quiz...")
    score_value = evaluate.start_quiz()
    total = len(evaluate.load_questions())
    score.display_score(name, score_value, total)
    score.save_score(name, score_value, total)

if __name__ == "__main__":
    while True:
        print("\n--- Online Quiz Application ---")
        print("1. Admin Login\n2. Take Quiz\n3. Exit")
        ch = input("Choose option: ")
        if ch == '1':
            admin_mode()
        elif ch == '2':
            user_mode()
        else:
            break
