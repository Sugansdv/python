# 13. Student Grade Calculator
# Concepts: functions, list, loop, strings.
# • Take student name and subject marks.
# • Calculate average, grade, and store in list.
# • Loop to handle multiple students.

students = []

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    marks = []
    for i in range(1, 4):
        mark = input(f"Enter mark {i}: ")
        if mark.isdigit():
            marks.append(int(mark))
        else:
            print("Invalid mark. Please enter a number.")
            return
    avg = sum(marks) / len(marks)
    grade = calculate_grade(avg)
    students.append([name, marks, avg, grade])
    print(f"{name}'s average: {avg:.2f}, Grade: {grade}\n")

while True:
    add_student()
    more = input("Add another student? (yes/no): ").strip().lower()
    if more != "yes":
        break

print("\n--- All Student Records ---")
for s in students:
    print(f"Name: {s[0]}, Marks: {s[1]}, Avg: {s[2]:.2f}, Grade: {s[3]}")
