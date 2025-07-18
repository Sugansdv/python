# main.py

from shift_utils import assign_shift, view_all_shifts

def main():
    while True:
        print("\n--- Employee Shift Tracker ---")
        print("1. Assign Shift")
        print("2. View All Assigned Shifts")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = (input("Enter Employee ID: "),)  # tuple form
            name = input("Enter Employee Name: ")
            shift = input("Enter Shift (e.g., Morning, Evening, Night): ")
            assign_shift(emp_id, name, shift)

        elif choice == "2":
            view_all_shifts()

        elif choice == "3":
            print("Exiting Shift Tracker.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
