TODO_FILE = "todo.txt"

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print(f"Task added: {task}")

def view_tasks():
    print("\nYour To-Do List:")
    try:
        with open(TODO_FILE, "r") as f:
            tasks = f.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

# Run Logic
while True:
    choice = input("\n1. Add Task\n2. View Tasks\n3. Exit\nChoose: ")
    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
