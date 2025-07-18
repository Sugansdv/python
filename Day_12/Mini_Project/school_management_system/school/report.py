from school.students.register import load_json as load_students
from school.teachers.register import load_json as load_teachers

def show_reports():
    students = load_students("data/students.json")
    teachers = load_teachers("data/teachers.json")

    print("\n---  Students ---")
    for s in students:
        print(f"{s['name']} (Grade {s['grade']})")

    print("\n---  Teachers ---")
    for t in teachers:
        print(f"{t['name']} - {t['subject']}")
