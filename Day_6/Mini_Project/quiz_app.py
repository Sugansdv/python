#16. Quiz App
# • Outer function calls inner quiz function
def start_quiz():
    score = 0

    # • Use conditionals to verify correct answers
    def quiz():
        nonlocal score
        print("Quiz Started!\n")

        q1 = input("1. What is the capital of France? ")
        if q1.lower() == "paris":
            score += 1

        q2 = input("2. What is 5 * 6? ")
        if q2 == "30":
            score += 1

        q3 = input("3. Who wrote 'Harry Potter'? ")
        if q3.lower() == "j.k. rowling":
            score += 1

    quiz()

    # • Return total score
    return score

# Run the quiz
final_score = start_quiz()
print(f"\nYour total score is: {final_score}/3")
