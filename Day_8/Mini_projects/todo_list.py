# 3. To-Do List Manager
# Description: Create a CLI-based daily planner.

# Store tasks in a list.
tasks = ["Buy groceries", "Finish assignment", "Call mom", "Workout", "Read book"]

# Loop through and print tasks with index using enumerate()
print("Your To-Do List:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# Mark tasks as complete (use remove() or pop())
completed_task = tasks.pop(1)  
print(f"\nCompleted Task: {completed_task}")

# Updated list after removing the completed task
print("\nUpdated To-Do List:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# Use slicing to show top priority tasks (first 3 tasks)
top_tasks = tasks[:3]
print("\nTop Priority Tasks:")
for task in top_tasks:
    print("-", task)
