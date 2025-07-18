import calendar
from datetime import datetime
from .tasks import _load_tasks

def show_calendar_tasks(month, year):
    tasks = _load_tasks()
    task_days = {int(t['due_date'].split('-')[2]) for t in tasks if t['due_date'].startswith(f"{year}-{month:02d}")}
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print("\nTasks Calendar:\n")
    for line in cal.formatmonth(year, month).splitlines():
        for day in task_days:
            line = line.replace(f"{day:2d}", f"[{day:2d}]")
        print(line)
