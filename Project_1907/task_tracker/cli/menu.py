from task_ops.manager import (
    add_task, complete_task, delete_task,
    show_overdue_tasks, group_by_priority
)

tasks = []

def run_menu():
    while True:
        print("\nTask Tracker Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Show Overdue Tasks")
        print("5. Group by Priority")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            complete_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            show_overdue_tasks(tasks)
        elif choice == "5":
            group_by_priority(tasks)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")
