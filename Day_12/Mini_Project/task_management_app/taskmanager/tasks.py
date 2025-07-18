import json
import os
from datetime import datetime

TASKS_FILE = "taskmanager/tasks.json"

def _load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def _save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(title, due_date, priority="Normal"):
    tasks = _load_tasks()
    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })
    _save_tasks(tasks)

def update_task(task_id, title=None, due_date=None):
    tasks = _load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if title: task['title'] = title
            if due_date: task['due_date'] = due_date
            break
    _save_tasks(tasks)

def delete_task(task_id):
    tasks = _load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    _save_tasks(tasks)

def list_tasks():
    tasks = _load_tasks()
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Due: {task['due_date']}, Priority: {task['priority']}, Done: {task['completed']}")
    return tasks
