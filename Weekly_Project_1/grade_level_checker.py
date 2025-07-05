# Grade Level Checker

# Input: total marks
total_marks = float(input("Enter the total marks obtained (out of 100): "))

# Use if-elif-else:
# 90: Excellent, 75–90: Good, 50–75: Average, else: Poor
if total_marks == 90:
    grade = "Excellent"
elif 75 <= total_marks < 90:
    grade = "Good"
elif 50 <= total_marks < 75:
    grade = "Average"
else:
    grade = "Poor"

# Use variable, float, condition
print("\n======= Grade Level Result =======")
print(f"Total Marks : {total_marks}")
print(f"Performance : {grade}")
print("==================================")
