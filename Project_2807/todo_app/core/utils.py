def today_tasks_generator(tasks):
    for task in tasks:
        if task.is_due_today():
            yield task
