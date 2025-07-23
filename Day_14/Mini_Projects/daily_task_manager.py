import os
from datetime import datetime

def get_today_filename():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"{today}.txt"

def add_task(task):
    filename = get_today_filename()
    with open(filename, "a") as f:
        f.write(task + "\n")
    print("Task added.")

def view_tasks():
    filename = get_today_filename()
    if not os.path.exists(filename):
        print("No tasks for today yet.")
        return

    with open(filename, "r") as f:
        tasks = f.readlines()

    if tasks:
        print("\n Today's Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")
    else:
        print("No tasks found.")

def delete_task(task_number):
    filename = get_today_filename()
    if not os.path.exists(filename):
        print("No task file for today.")
        return

    with open(filename, "r") as f:
        tasks = f.readlines()

    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        with open(filename, "w") as f:
            f.writelines(tasks)
        print(f"Task deleted: {removed_task.strip()}")
    else:
        print("Invalid task number.")

def main():
    print("=== Daily Task Manager ===")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
