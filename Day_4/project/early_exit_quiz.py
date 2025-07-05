# ==== MINI PROJECT 8: EARLY EXIT QUIZ ====

print("====================")
print("Early Exit Quiz")
print("====================")

# Ask 5 simple questions
questions = [
    ("What is the capital of India?", "Delhi"),
    ("What is 5 + 3?", "8"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What color do you get by mixing red and white?", "Pink"),
    ("How many days are there in a week?", "7")
]

# Loop through questions
for question, correct_answer in questions:
    user_answer = input(question + " ")
    
    # If wrong answer is given, exit loop and display "Game Over"
    if user_answer.strip().lower() != correct_answer.lower():
        print("Game Over! Wrong answer.")
        break
else:
    # If loop completes, show “Quiz Completed”
    print("Quiz Completed! You answered all questions correctly.")
