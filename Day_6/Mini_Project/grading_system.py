#  2. Student Grading System

# • Function to input marks for 5 subjects
def get_marks():
    marks = []
    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return marks

# • Return average and grade using conditional logic
def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 35:
        grade = "D"
    else:
        grade = "F"
        
    return avg, grade

# • Use recursion for re-evaluation if marks < 35
def evaluate_student():
    marks = get_marks()
    
    # Check for any subject mark less than 35
    if any(mark < 35 for mark in marks):
        print(" One or more marks are below 35. Please re-enter all marks.")
        return evaluate_student()  # Recursively call for re-evaluation
    
    avg, grade = calculate_grade(marks)
    print(f" Average Marks: {avg}")
    print(f"🎓 Grade: {grade}")

evaluate_student()
