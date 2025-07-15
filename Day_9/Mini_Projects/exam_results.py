# 14. Exam Result Processing
# Goal: Store and analyze student exam results.
# Requirements:
# • Store results as: (student_name, (subject1_score, subject2_score, ...))
# • Calculate total and average using sum(), len().
# • Use indexing to access specific subject.
# • Tuple immutability ensures original scores aren't altered.

# List of student results
results = [
    ("Alice", (85, 92, 78)),
    ("Bob", (75, 80, 68)),
    ("Charlie", (90, 88, 94)),
    ("David", (60, 72, 70)),
    ("Eva", (95, 98, 92))
]

# Process and display results
print(" Exam Result Report:\n")
for name, scores in results:
    total = sum(scores)
    average = total / len(scores)
    print(f"Student: {name}")
    print(f"  Subject 1: {scores[0]}")
    print(f"  Subject 2: {scores[1]}")
    print(f"  Subject 3: {scores[2]}")
    print(f"  Total: {total}, Average: {average:.2f}")
    print("-" * 30)
