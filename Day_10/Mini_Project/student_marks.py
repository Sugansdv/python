# 1. Student Marks Manager
# Description: Manage marks for students across different subjects.
# Requirements:
# - Dictionary format: {student_name: {subject: mark}}
# - Add new students and subjects
# - Update marks using nested access
# - Remove student or subject
# - List all students and their average marks
# - Identify topper by comparing total marks
# - Use .get() to handle missing data
# - Apply dictionary comprehension to list passed students (avg > 50)

student_marks = {
    "Alice": {"Math": 80, "Science": 70},
    "Bob": {"Math": 40, "Science": 45},
    "Charlie": {"Math": 90, "Science": 95}
}

def add_or_update_mark(student, subject, mark):
    student_marks.setdefault(student, {})[subject] = mark

def remove_student(student):
    student_marks.pop(student, None)

def remove_subject(student, subject):
    if student in student_marks:
        student_marks[student].pop(subject, None)

def list_all_averages():
    for student, subjects in student_marks.items():
        avg = sum(subjects.values()) / len(subjects) if subjects else 0
        print(f"{student}: Avg = {avg:.2f}")

def get_topper():
    return max(student_marks.items(), key=lambda x: sum(x[1].values()))

def list_passed_students():
    return {s: avg for s, avg in ((k, sum(v.values()) / len(v)) for k, v in student_marks.items()) if avg > 50}
