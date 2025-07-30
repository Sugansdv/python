import os
from datetime import datetime
from core.task import Task
from core.decorators import timeit

class TaskManager:
    def __init__(self, filepath="data/tasks.txt"):
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        name = parts[0].strip()
                        deadline_str = parts[1].strip().split("-")
                        deadline = tuple(map(int, deadline_str))
                        status = parts[2].strip()
                        self.tasks.append(Task(name, deadline, status))

    def save_tasks(self):
        with open(self.filepath, "w") as f:
            for task in self.tasks:
                deadline = "-".join(map(str, task.deadline))
                f.write(f"{task.name} | {deadline} | {task.status}\n")

    @timeit
    def add_task(self, name, deadline_str):
        try:
            date_obj = datetime.strptime(deadline_str, "%Y-%m-%d")
            deadline = (date_obj.year, date_obj.month, date_obj.day)
            self.tasks.append(Task(name, deadline))
            print("Task added.")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name and task.status == "Pending":
                task.status = "Completed"
                print("Task marked as completed.")
                return
        print("Task not found or already completed.")

    def delete_task(self, name):
        before = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.name != name]
        if len(self.tasks) < before:
            print("Task deleted.")
        else:
            print("Task not found.")
