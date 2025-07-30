from datetime import datetime

class Task:
    def __init__(self, name, deadline, status="Pending"):
        self.name = name
        self.deadline = deadline  # tuple: (YYYY, MM, DD)
        self.status = status

    def is_overdue(self):
        today = datetime.today().date()
        return datetime(*self.deadline).date() < today and self.status == "Pending"

    def is_due_today(self):
        today = datetime.today().date()
        return datetime(*self.deadline).date() == today and self.status == "Pending"

    def __str__(self):
        deadline_str = f"{self.deadline[0]:04d}-{self.deadline[1]:02d}-{self.deadline[2]:02d}"
        status = f"[{'OVERDUE' if self.is_overdue() else self.status}]"
        return f"{self.name} | Due: {deadline_str} | {status}"
