import sys
import os

# Add project root to path for absolute imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from school.students.register import register_student
from school.teachers.register import register_teacher
from school.subjects.assign import assign_subject
from school.report import show_reports

def main():
    while True:
        print("\n School Management System")
        print("1. Register Student")
        print("2. Register Teacher")
        print("3. Assign Subject")
        print("4. Show Reports")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Student Name: ")
            grade = input("Grade: ")
            register_student(name, grade)
        elif choice == '2':
            name = input("Teacher Name: ")
            subject = input("Subject: ")
            register_teacher(name, subject)
        elif choice == '3':
            subject = input("Subject: ")
            teacher = input("Teacher Name: ")
            assign_subject(subject, teacher)
        elif choice == '4':
            show_reports()
        elif choice == '5':
            print(" Exiting...")
            break
        else:
            print(" Invalid option.")

if __name__ == "__main__":
    main()
