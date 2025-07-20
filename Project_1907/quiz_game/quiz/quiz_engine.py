import random

def ask_question(q):
    print(f"\n{q['question']}")
    for i, option in enumerate(q['options'], 1):
        print(f"{i}. {option}")
    try:
        ans = int(input("Your answer (1-4): "))
        return q['options'][ans - 1] == q['answer']
    except (IndexError, ValueError):
        print("Invalid choice.")
        return False

def run_quiz(questions):
    score = 0
    asked = set()
    total = min(len(questions), 5)
    topics = set()

    print(f"Starting quiz with {total} questions...")

    for _ in range(total):
        q = random.choice([q for q in questions if q['question'] not in asked])
        asked.add(q['question'])
        topics.add(q['topic'])
        if ask_question(q):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. Correct answer: {q['answer']}")

    print(f"\n🎓 Quiz Complete! You scored {score}/{total}")
    print(f"📚 Topics Covered: {', '.join(sorted(topics))}")
