from core.manager import TaskManager
from core.utils import today_tasks_generator

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. View Overdue Tasks")
    print("6. View Tasks Due Today")
    print("7. Exit")

def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Task name: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            manager.add_task(name, deadline)

        elif choice == "2":
            name = input("Task name to complete: ")
            manager.complete_task(name)

        elif choice == "3":
            name = input("Task name to delete: ")
            manager.delete_task(name)

        elif choice == "4":
            for task in manager.tasks:
                print(task)

        elif choice == "5":
            for task in manager.tasks:
                if task.is_overdue():
                    print(task)

        elif choice == "6":
            for task in today_tasks_generator(manager.tasks):
                print(task)

        elif choice == "7":
            manager.save_tasks()
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
