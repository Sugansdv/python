from .marks import calculate_average
from .grade import calculate_cgpa, get_grade

def generate_report(student_name, subject_marks):
    averages = [calculate_average(marks) for marks in subject_marks.values()]
    cgpa = round(calculate_cgpa(averages), 2)
    grade = get_grade(cgpa)

    return {
        "student": student_name,
        "CGPA": cgpa,
        "Grade": grade
    }
