# 4. Simple Task Manager 
# Concepts: while menu loop, string operations, lists.
# • Tasks stored in a list.
# • Add, delete, mark complete using menu options.
# • Display using formatted string output.
# • Use functions for modularity.

tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "status": "Pending"})

def delete_task():
    show_tasks()
    index = input("Enter task number to delete: ")
    if index.isdigit() and 1 <= int(index) <= len(tasks):
        tasks.pop(int(index) - 1)

def mark_complete():
    show_tasks()
    index = input("Enter task number to mark complete: ")
    if index.isdigit() and 1 <= int(index) <= len(tasks):
        tasks[int(index) - 1]["status"] = "Done"

def show_tasks():
    if not tasks:
        print("No tasks to show.\n")
    else:
        print("\n--- Task List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} [{task['status']}]")
        print()

while True:
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Complete")
    print("4. Show All Tasks")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        show_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice.\n")

