from gradebook.student_ops import (
    add_student, update_grades, calculate_averages, find_top_students
)
from gradebook.report_gen import generate_report_card

def get_input(prompt):
    return input(prompt).strip()

def main():
    students = []

    while True:
        print("\n🎓 Student Gradebook")
        print("1. Add Student")
        print("2. Update Grades")
        print("3. Generate Report Card")
        print("4. Calculate Averages")
        print("5. Top Performers")
        print("6. List Subjects")
        print("7. Exit")

        choice = get_input("Choose (1-7): ")

        if choice == "1":
            roll = get_input("Enter Roll Number: ")
            name = get_input("Enter Name: ")
            add_student(students, roll, name)

        elif choice == "2":
            roll = get_input("Enter Roll Number: ")
            subject = get_input("Enter Subject: ")
            marks = float(get_input("Enter Marks: "))
            update_grades(students, roll, subject, marks)

        elif choice == "3":
            roll = get_input("Enter Roll Number to print report: ")
            generate_report_card(students, roll)

        elif choice == "4":
            calculate_averages(students)

        elif choice == "5":
            find_top_students(students)

        elif choice == "6":
            subjects = set()
            for student in students:
                subjects.update(student['grades'].keys())
            print(" Subjects:", ', '.join(sorted(subjects)))

        elif choice == "7":
            print(" Exiting Gradebook.")
            break

        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main()
