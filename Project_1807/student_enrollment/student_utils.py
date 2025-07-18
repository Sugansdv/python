

from data.available_courses import available_courses

def add_student(students, student_id, name):
    if student_id in students:
        print("Student already exists.")
        return
    students[student_id] = {
        "name": name,
        "courses": set()
    }
    print(f"Student '{name}' added successfully.")

def enroll_course(students, student_id, course):
    if course not in available_courses:
        print(f"Course '{course}' is not available.")
        return
    if student_id not in students:
        print("Student not found.")
        return
    if course in students[student_id]["courses"]:
        print("Student already enrolled in this course.")
    else:
        students[student_id]["courses"].add(course)
        print(f"'{course}' added for {students[student_id]['name']}.")

def drop_course(students, student_id, course):
    if student_id not in students:
        print("Student not found.")
        return
    if course in students[student_id]["courses"]:
        students[student_id]["courses"].remove(course)
        print(f"'{course}' dropped for {students[student_id]['name']}.")
    else:
        print(f"{students[student_id]['name']} is not enrolled in '{course}'.")

def show_student_info(students, student_id):
    if student_id not in students:
        print("Student not found.")
        return
    info = students[student_id]
    print(f"\nStudent ID: {student_id}")
    print(f"Name: {info['name']}")
    print(f"Enrolled Courses: {', '.join(info['courses']) if info['courses'] else 'None'}")
