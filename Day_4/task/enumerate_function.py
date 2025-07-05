# Task 31: Use enumerate() to print index and value for "Python"
for index, char in enumerate("Python"):
    print(f"Index {index}: {char}")

print('-' * 30)

# Task 32: Use enumerate() with a fruit list to print like: 1. Apple  2. Banana  3. Cherry
fruits = ["Apple", "Banana", "Cherry"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")

print('-' * 30)

# Task 33: Use enumerate() to display character positions in "Hello World"
for index, char in enumerate("Hello World"):
    print(f"Position {index}: {char}")

print('-' * 30)

# Task 34: Create a list of students and print roll number using enumerate(start=101)
students = ["Arun", "Banu", "Charan", "Divya"]
for roll_no, name in enumerate(students, start=101):
    print(f"Roll No {roll_no}: {name}")

print('-' * 30)

# Task 35: Use enumerate() inside a function that labels each item in a menu list
def print_menu(menu_items):
    print("Menu:")
    for i, item in enumerate(menu_items, start=1):
        print(f"{i}. {item}")

menu = ["Pizza", "Burger", "Pasta", "Juice"]
print_menu(menu)
