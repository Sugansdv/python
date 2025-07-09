# 19. Quiz with Exit Option
# Objective: Ask user 5 questions and allow early exit.

# • Use a list of questions.
questions = [
    "What is the capital of India?",
    "What is 5 + 7?",
    "Which planet is known as the Red Planet?",
    "What is the boiling point of water in Celsius?",
    "Who wrote the national anthem of India?"
]

i = 0

# • Use while to iterate through them.
while i < len(questions):
    answer = input(f"Q{i+1}: {questions[i]} (type 'quit' to exit): ").strip()

    # • Use break if user types "quit".
    if answer.lower() == "quit":
        print(" Quiz exited early by user.")
        break

    i += 1

# • Use else to show “Quiz complete” message.
else:
    print("\n Quiz complete. Thanks for participating!")
