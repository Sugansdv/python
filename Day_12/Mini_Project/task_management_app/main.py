from taskmanager import add_task, update_task, delete_task, list_tasks, set_priority, show_calendar_tasks

def main():
    while True:
        print("\n--- Task Management System ---")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Set Priority")
        print("6. Calendar View")
        print("7. Exit")

        choice = input("Choose: ")
        if choice == '1':
            title = input("Enter task title: ")
            due = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, due)
        elif choice == '2':
            task_id = int(input("Task ID: "))
            title = input("New Title (leave blank to skip): ")
            due = input("New Due Date (YYYY-MM-DD): ")
            update_task(task_id, title or None, due or None)
        elif choice == '3':
            task_id = int(input("Task ID to delete: "))
            delete_task(task_id)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            task_id = int(input("Task ID: "))
            level = input("Priority (Low, Normal, High): ")
            set_priority(task_id, level)
        elif choice == '6':
            year = int(input("Year: "))
            month = int(input("Month (1-12): "))
            show_calendar_tasks(month, year)
        else:
            break

if __name__ == "__main__":
    main()
