
from grade_utils import calculator

# (student_id, name): {subject: mark}
student_records = {}

def add_student(student_id, name, marks_dict):
    subjects = calculator.validate_subjects(marks_dict.keys())

    key = (student_id, name)
    if key in student_records:
        print("Student already added!")
        return

    student_records[key] = marks_dict
    print(f"Student {name} added with subjects: {', '.join(subjects)}")


def show_report():
    print("\n--- Student Grade Report ---")
    for (student_id, name), marks in student_records.items():
        avg = calculator.calculate_average(marks)
        grade = calculator.assign_grade(avg)
        print(f"\nID: {student_id}, Name: {name}")
        for sub, mark in marks.items():
            print(f"  {sub}: {mark}")
        print(f"  Average: {avg:.2f}, Grade: {grade}")


if __name__ == "__main__":
    add_student("S001", "Alice", {"Math": 85, "English": 92, "Science": 78})
    add_student("S002", "Bob", {"Math": 55, "English": 62, "History": 48})
    add_student("S003", "Charlie", {"Biology": 95, "Chemistry": 88, "Physics": 91})

    show_report()
