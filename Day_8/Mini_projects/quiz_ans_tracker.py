# 11. Quiz Answer Tracker
# Description: Store and evaluate quiz answers.

# Correct answers (predefined)
correct_answers = ['A', 'C', 'B', 'D', 'A']

# User inputs stored in a list
user_answers = ['A', 'B', 'B', 'D', 'C'] 

# Compare with correct answers using index and count correct/incorrect
correct = 0
incorrect = 0

print(" Quiz Evaluation:")

for i in range(len(correct_answers)):
    print(f"Q{i+1}: Your Answer = {user_answers[i]}, Correct Answer = {correct_answers[i]}")
    if user_answers[i] == correct_answers[i]:
        correct += 1
    else:
        incorrect += 1

# Count total correct/incorrect answers
print(f"\nTotal Correct Answers: {correct}")
print(f"Total Incorrect Answers: {incorrect}")
