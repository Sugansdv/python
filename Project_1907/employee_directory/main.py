from directory.operations import add_employee, remove_employee, update_employee
from search.lookup import search_by_name, search_by_department
from utils.helpers import list_departments

employees = []

def main():
    while True:
        print("\nEmployee Directory")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search by Name")
        print("5. Search by Department")
        print("6. List Departments")
        print("7. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            emp_id = input("Enter ID: ").strip()
            name = input("Enter Name: ").strip()
            dept = input("Enter Department: ").strip()
            add_employee(employees, (emp_id,), name, dept)

        elif choice == "2":
            emp_id = input("Enter ID to remove: ").strip()
            remove_employee(employees, emp_id)

        elif choice == "3":
            emp_id = input("Enter ID to update: ").strip()
            name = input("New Name: ").strip()
            dept = input("New Department: ").strip()
            update_employee(employees, emp_id, name, dept)

        elif choice == "4":
            name = input("Enter name to search: ").strip()
            search_by_name(employees, name)

        elif choice == "5":
            dept = input("Enter department to search: ").strip()
            search_by_department(employees, dept)

        elif choice == "6":
            list_departments(employees)

        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
