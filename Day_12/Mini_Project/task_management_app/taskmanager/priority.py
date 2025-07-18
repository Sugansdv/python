from .tasks import _load_tasks, _save_tasks

def set_priority(task_id, level):
    tasks = _load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['priority'] = level
            break
    _save_tasks(tasks)
