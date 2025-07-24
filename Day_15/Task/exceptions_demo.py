# 1. Divide two numbers, handle ZeroDivisionError and ValueError.
def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter integers.")

# 2. Take user input for age, raise error if input is non-numeric or negative.
def input_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print("Your age is:", age)
    except ValueError as ve:
        print("Error:", ve)

# 3. Open a file, handle FileNotFoundError.
def open_file():
    try:
        with open("non_existent_file.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found.")

# 4. Read from a closed file, handle ValueError.
def read_closed_file():
    try:
        f = open("temp.txt", "w")
        f.write("Test")
        f.close()
        print(f.read())  # Error: file is closed
    except ValueError as ve:
        print("Error:", ve)

# 5. Handle IndexError when accessing list items by user input index.
def access_list():
    items = [10, 20, 30]
    try:
        index = int(input("Enter index (0–2): "))
        print("Item:", items[index])
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid number.")

# 6. Handle KeyError when accessing a dictionary with a missing key.
def access_dict():
    data = {'name': 'John', 'age': 30}
    try:
        key = input("Enter key to access (name/age): ")
        print("Value:", data[key])
    except KeyError:
        print("Error: Key not found in dictionary.")

# 7. Ask user to enter a number, convert to int, catch ValueError.
def convert_to_int():
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Error: That's not a valid integer.")

# 8. Catch TypeError when trying to add string and integer.
def add_str_and_int():
    try:
        result = "Age: " + 25
        print(result)
    except TypeError as te:
        print("Error:", te)

# 9. Catch AttributeError by calling a non-existent method on an object.
def call_nonexistent_method():
    try:
        text = "hello"
        text.run()  # This method does not exist
    except AttributeError as ae:
        print("Error:", ae)

# 10. Handle NameError when accessing an undefined variable.
def access_undefined_var():
    try:
        print(xyz)  # xyz is not defined
    except NameError as ne:
        print("Error:", ne)

# Call all functions 
if __name__ == "__main__":
    divide_numbers()
    input_age()
    open_file()
    read_closed_file()
    access_list()
    access_dict()
    convert_to_int()
    add_str_and_int()
    call_nonexistent_method()
    access_undefined_var()
