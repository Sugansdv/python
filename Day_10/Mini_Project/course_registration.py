# 17. College Course Registration
# Description: Manage student-course enrollments.
# Requirements:
# - {student_name: [courses]}
# - Add/drop course
# - Show all students in a course
# - Use in and not in for checks

registrations = {
    "Alice": ["Math", "Physics"],
    "Bob": ["Chemistry", "Math"],
    "Charlie": ["Biology"]
}

def add_course(student, course):
    if student in registrations:
        if course not in registrations[student]:
            registrations[student].append(course)
            print(f"Course '{course}' added for {student}.")
        else:
            print(f"{student} is already enrolled in '{course}'.")
    else:
        registrations[student] = [course]
        print(f"{student} registered with course '{course}'.")

def drop_course(student, course):
    if student in registrations and course in registrations[student]:
        registrations[student].remove(course)
        print(f"Course '{course}' dropped for {student}.")
    else:
        print(f"{student} is not enrolled in '{course}' or does not exist.")

def show_students_in_course(course):
    print(f"\nStudents enrolled in '{course}':")
    found = False
    for student, courses in registrations.items():
        if course in courses:
            print(student)
            found = True
    if not found:
        print("No students enrolled in this course.")

add_course("Alice", "Chemistry")
add_course("David", "Math")
drop_course("Bob", "Math")
drop_course("Charlie", "Math")  # Not enrolled
show_students_in_course("Math")
