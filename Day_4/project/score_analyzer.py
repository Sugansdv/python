# ==== MINI PROJECT 4: STUDENT SCORE ANALYZER ====

print("====================")
print("Student Score Analyzer")
print("====================")

# Use a for loop to collect 5 marks
# Store in a list
marks = []
for i in range(5):
    score = int(input(f"Enter mark {i+1}: "))
    marks.append(score)

# Calculate max using loop
max_score = marks[0]
for mark in marks:
    if mark > max_score:
        max_score = mark

# Calculate min using loop
min_score = marks[0]
for mark in marks:
    if mark < min_score:
        min_score = mark

# Calculate sum using loop → average
total = 0
for mark in marks:
    total += mark
average = total / len(marks)

# Display results
print("\nAnalysis Result:")
print(f"Highest Score: {max_score}")
print(f"Lowest Score : {min_score}")
print(f"Average Score: {average:.2f}")
