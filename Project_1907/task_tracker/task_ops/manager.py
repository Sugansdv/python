from datetime import datetime

def add_task(tasks):
    title = input("Title: ").strip()
    due_date = input("Due date (YYYY-MM-DD): ").strip()
    priority = input("Priority (High/Medium/Low): ").strip()
    tags = set(input("Tags (comma-separated): ").strip().split(","))
    notes = input("Notes: ").strip()

    try:
        due = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    task = {
        "info": (title, due),
        "priority": priority,
        "tags": tags,
        "notes": notes,
        "done": False
    }
    tasks.append(task)
    print("Task added.")

def complete_task(tasks):
    title = input("Enter title of task to mark complete: ").strip()
    for task in tasks:
        if task["info"][0] == title:
            task["done"] = True
            print("Marked as complete.")
            return
    print("Task not found.")

def delete_task(tasks):
    title = input("Enter title of task to delete: ").strip()
    for i, task in enumerate(tasks):
        if task["info"][0] == title:
            del tasks[i]
            print("Task deleted.")
            return
    print("Task not found.")

def show_overdue_tasks(tasks):
    today = datetime.today().date()
    print("Overdue Tasks:")
    for task in tasks:
        if not task["done"] and task["info"][1] < today:
            print(f"- {task['info'][0]} (Due: {task['info'][1]})")

def group_by_priority(tasks):
    groups = {}
    for task in tasks:
        key = task["priority"]
        groups.setdefault(key, []).append(task)

    for p, group in groups.items():
        print(f"Priority: {p}")
        for t in group:
            status = "Done" if t["done"] else "Pending"
            print(f"  - {t['info'][0]} (Due: {t['info'][1]}, Tags: {', '.join(t['tags'])}, {status})")
