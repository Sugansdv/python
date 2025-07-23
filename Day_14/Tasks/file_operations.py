# 1. Create a new text file and write a welcome message
with open("welcome.txt", "w") as file:
    file.write("Welcome to basic file operations in Python!\n")

# 2. Open a file, write multiple lines, and close it manually
file = open("multilines.txt", "w")
file.write("Line 1: Hello!\n")
file.write("Line 2: This is the second line.\n")
file.write("Line 3: Goodbye!\n")
file.close()

# 3. Use the with statement to read a file without manually closing it
with open("welcome.txt", "r") as file:
    content = file.read()
    print("\n3. With statement read:\n", content)

# 4. Read the contents of a file using .read()
file = open("multilines.txt", "r")
content = file.read()
print("4. Using .read():\n", content)
file.close()

# 5. Read a file line-by-line using .readline()
file = open("multilines.txt", "r")
print("5. Using .readline():")
print(file.readline(), end='')  # Line 1
print(file.readline(), end='')  # Line 2
file.close()

# 6. Read all lines of a file into a list using .readlines()
with open("multilines.txt", "r") as file:
    lines = file.readlines()
    print("6. Using .readlines():\n", lines)

# 7. Write a function that takes user input and appends it to a file
def append_user_input(filename):
    user_input = input("7. Enter something to append to the file: ")
    with open(filename, "a") as file:
        file.write(user_input + "\n")

# Uncomment to test it:
append_user_input("user_input.txt")

# 8. Write and overwrite a file using 'w' mode
with open("overwrite.txt", "w") as file:
    file.write("This will overwrite any existing content.\n")

# 9. Append data to a file using 'a' mode and then display the full content
with open("overwrite.txt", "a") as file:
    file.write("This line is appended.\n")

with open("overwrite.txt", "r") as file:
    print("9. Appended and read full content:\n", file.read())

# 10. Use 'x' mode to create a file, and handle the error if it already exists
try:
    with open("unique_file.txt", "x") as file:
        file.write("This file was created using 'x' mode.\n")
    print("10. 'unique_file.txt' created successfully.")
except FileExistsError:
    print("10. Error: 'unique_file.txt' already exists.")
