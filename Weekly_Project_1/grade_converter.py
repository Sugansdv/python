# Marks to Grade Converter

# Input list of marks
input_str = input("Enter marks of students (comma-separated): ")
marks_list = [int(mark.strip()) for mark in input_str.split(",")]

# Use for loop with if-elif-else inside loop to print grades
print("\n======== Marks to Grades =========")
for mark in marks_list:
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Marks: {mark} → Grade: {grade}")
print("==================================")
