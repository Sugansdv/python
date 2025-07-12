# 20. Pattern Generator
# Concepts: while loop, string operations.
# • Print star, triangle, number patterns.
# • User chooses type and size.
# • Use nested loops.

def star_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def triangle_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

while True:
    print("\n1. Star Pattern")
    print("2. Number Pattern")
    print("3. Triangle Pattern")
    print("4. Exit")
    choice = input("Choose a pattern: ")

    if choice in ["1", "2", "3"]:
        size = input("Enter size: ")
        if size.isdigit():
            size = int(size)
            if choice == "1":
                star_pattern(size)
            elif choice == "2":
                number_pattern(size)
            elif choice == "3":
                triangle_pattern(size)
        else:
            print("Invalid size.\n")
    elif choice == "4":
        break
    else:
        print("Invalid option.\n")
