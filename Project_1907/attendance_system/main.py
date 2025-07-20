from core.attendance import (
    mark_attendance,
    view_by_date,
    view_by_student,
    show_absentees,
)
from core.data.store import load_data, save_data

def main():
    students, attendance = load_data()

    while True:
        print("\nAttendance System Menu")
        print("1. Mark Attendance")
        print("2. View Attendance by Date")
        print("3. View Attendance by Student")
        print("4. Show Absentees by Date")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            mark_attendance(students, attendance)
        elif choice == "2":
            view_by_date(attendance)
        elif choice == "3":
            view_by_student(students, attendance)
        elif choice == "4":
            show_absentees(students, attendance)
        elif choice == "5":
            save_data(students, attendance)
            print("Exiting. Data saved.")
            break
        else:
            print("Invalid choice.")
    
if __name__ == "__main__":
    main()
