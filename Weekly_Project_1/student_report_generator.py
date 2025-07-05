# Student Report Card Generator

# Use variables to store student name, class, and marks (list).
student_name = "Dharun Viashwa"
student_class = "10th Grade"
marks = [85, 92, 78, 88, 90]  

# Use a for loop to calculate total and average.
total_marks = 0
for mark in marks:
    total_marks += mark

average_marks = total_marks / len(marks)

# Use if-elif-else to assign grade: ≥90: A, 80–89: B, 70–79: C, else: D.
if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 70:
    grade = "C"
else:
    grade = "D"

# Print Report Card using f-string
print("\n===== Student Report Card =====")
print(f"Name       : {student_name}")
print(f"Class      : {student_class}")
print(f"Marks      : {marks}")
print(f"Total      : {total_marks}")
print(f"Average    : {average_marks:.2f}")
print(f"Grade      : {grade}")
print("================================")
