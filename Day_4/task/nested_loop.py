# Task 36: Multiplication table for numbers 1 to 3 using nested loops
for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)

# Task 37: Nested loop to print this pattern: * * ** * ** * * *
pattern = [0,1, 2, 3, 4]
for count in pattern:
    for _ in range(count):
        print("*", end=" ")
    print()

# Task 38: Number triangle
for i in range(2, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Task 39: All pair combinations from two lists
colors = ["Red", "Green"]
shapes = ["Circle", "Square"]
for color in colors:
    for shape in shapes:
        print(f"{color} - {shape}")

# Task 40: Multiplication chart from 1x1 to 5x5
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()

# Task 41: Right-angled triangle with alphabets: A B B \n C C C
letter = ord('A')
for i in range(1, 4):
    for j in range(i):
        print(chr(letter), end=" ")
    letter += 1
    print()

# Task 42: User name triangle pattern
name = input("Enter your name for Task 42: ")
for i in range(1, len(name) + 1):
    for j in range(i):
        print(name[j], end=" ")
    print()

# Task 43: Pattern like:
# 2 2
# 3 3 3
# 4 4 4 4
for i in range(2, 5):
    for j in range(i):
        print(i, end=" ")
    print()

# Task 44: Print a 3x3 grid using nested loops
for i in range(3):
    for j in range(3):
        print("#", end=" ")
    print()

# Task 45: Star pattern with custom rows and columns
rows = int(input("Enter number of rows for Task 45: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
