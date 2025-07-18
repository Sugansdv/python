from student_utils import add_student, enroll_course, drop_course, show_student_info

def main():
    students = {}

    while True:
        print("\n--- Student Enrollment System ---")
        print("1. Add Student")
        print("2. Enroll in Course")
        print("3. Drop Course")
        print("4. Show Student Info")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            raw_id = input("Enter Student ID (e.g., 1001): ")
            student_id = (raw_id,)  # Tuple form
            name = input("Enter student name: ")
            add_student(students, student_id, name)

        elif choice == "2":
            raw_id = input("Enter Student ID: ")
            student_id = (raw_id,)
            course = input("Enter course to enroll: ")
            enroll_course(students, student_id, course)

        elif choice == "3":
            raw_id = input("Enter Student ID: ")
            student_id = (raw_id,)
            course = input("Enter course to drop: ")
            drop_course(students, student_id, course)

        elif choice == "4":
            raw_id = input("Enter Student ID: ")
            student_id = (raw_id,)
            show_student_info(students, student_id)

        elif choice == "5":
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
