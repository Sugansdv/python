## 11. To-Do List Manager
print("========================================")
print("            To-Do List Manager          ")
print("========================================")

# 1. Let the user add three tasks
task1 = input("Enter Task 1: ")
task2 = input("Enter Task 2: ")
task3 = input("Enter Task 3: ")

# 2. Store tasks in a list
todo_list = [task1, task2, task3]

# 3. Print the full list
print("\n Your To-Do List:")
print(todo_list)

# 4. Print each task with its number (index + 1)
print("\n Tasks with Numbers:")
for index, task in enumerate(todo_list, start=1):
    print(f"{index}. {task}")
