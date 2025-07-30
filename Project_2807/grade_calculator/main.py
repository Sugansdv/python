from core.student import Student
from core.manager import StudentManager
from core.utils import grade_a_students, unique_subjects

def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Grade Calculator ---")
        print("1. Add Student")
        print("2. View Top Student")
        print("3. View Class Average")
        print("4. Export Grades to CSV")
        print("5. List Grade 'A' Students")
        print("6. Show Unique Subjects")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            sid = input("ID: ")
            name = input("Name: ")
            subjects = input("Enter subjects (comma-separated): ").split(",")
            marks = {}
            for subj in subjects:
                score = float(input(f"Marks for {subj.strip()}: "))
                marks[subj.strip()] = score
            try:
                student = Student(sid, name, marks)
                manager.add_student(student)
                print("Student added.")
            except ValueError as e:
                print("Error:", e)

        elif choice == '2':
            top = manager.top_student()
            if top:
                print(f"Top Student: {top.name} | Avg: {top.average():.2f} | Grade: {top.grade()}")
            else:
                print("No students yet.")

        elif choice == '3':
            avg = manager.class_average()
            print(f"Class Average: {avg:.2f}")

        elif choice == '4':
            manager.export_grades()
            print("Grades exported to data/grades.csv.")

        elif choice == '5':
            for student in grade_a_students(manager.students):
                print(f"{student.name} ({student.id}) - Grade A")

        elif choice == '6':
            print("Subjects:", unique_subjects(manager.students))

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
