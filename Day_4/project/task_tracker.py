# ==== MINI PROJECT 16: WEEKLY TASK TRACKER ====

print("====================")
print("Weekly Task Tracker")
print("====================")

# Predefined task list
tasks = ["Submit report", "Team meeting", "Code review", "Client call", "Documentation", "Testing", "Planning"]

# Days of the week starting from Monday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Use loop with enumerate() starting from Monday
for index, task in enumerate(tasks):
    # Output format: Monday: Task
    print(f"{days[index]}: {task}")
