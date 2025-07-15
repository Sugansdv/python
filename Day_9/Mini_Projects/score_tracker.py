# 1. Student Score Tracker
# Goal: Maintain and display student names with their subject scores using tuples.
# Requirements:
# • Use a tuple to store each student’s data: (name, (math, physics, chemistry))
# • Access subject-wise scores using indexing.
# • Find average marks per student using sum() and len().
# • Unpack each tuple to display name and subjects separately.
# • Prevent accidental modification using tuple immutability.

students = [
    ("Alice", (85, 90, 88)),
    ("Bob", (78, 82, 80)),
    ("Charlie", (92, 88, 95)),
    ("David", (70, 75, 72)),
]

print(" Student Score Tracker\n")

for student in students:
    name, scores = student
    math = scores[0]
    physics = scores[1]
    chemistry = scores[2]
    avg = sum(scores) / len(scores)

    print(f"Name: {name}")
    print(f"  Math: {math}")
    print(f"  Physics: {physics}")
    print(f"  Chemistry: {chemistry}")
    print(f"  Average: {avg:.2f}")
    print("-" * 30)
