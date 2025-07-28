import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Enter task title: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

    task = {
        "title": title,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print(" Task added!")

def view_tasks(tasks, show_all=True):
    if not tasks:
        print("📭 No tasks to display.")
        return

    print("\n Task List:")
    for i, task in enumerate(tasks, start=1):
        if not show_all and task["completed"]:
            continue
        status = "completed" if task["completed"] else "not completed"
        print(f"{i}. {task['title']} | Due: {task['due_date']} | Priority: {task['priority']} | Status: {status}")
    print()

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        print(f" Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print(" Invalid task number.")

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        tasks[index]["completed"] = True
        print(f" Marked '{tasks[index]['title']}' as complete!")
    except (ValueError, IndexError):
        print(" Invalid task number.")

def sort_tasks(tasks):
    option = input("Sort by (1) Priority or (2) Due Date? ").strip()
    if option == '1':
        priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
        tasks.sort(key=lambda x: priority_order.get(x['priority'], 4))
        print(" Sorted by priority.")
    elif option == '2':
        tasks.sort(key=lambda x: datetime.strptime(x['due_date'], "%Y-%m-%d"))
        print(" Sorted by due date.")
    else:
        print(" Invalid sort option.")

def search_tasks(tasks):
    keyword = input("Enter keyword to search: ").strip().lower()
    found = [task for task in tasks if keyword in task["title"].lower()]
    if found:
        print("\n Search Results:")
        view_tasks(found)
    else:
        print(" No matching tasks found.")

def main():
    tasks = load_tasks()

    while True:
        print("""
=====  To-Do List Menu =====
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Sort Tasks
6. Search Task
7. Exit
""")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_complete(tasks)
        elif choice == '5':
            sort_tasks(tasks)
        elif choice == '6':
            search_tasks(tasks)
        elif choice == '7':
            save_tasks(tasks)
            print(" Tasks saved. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
