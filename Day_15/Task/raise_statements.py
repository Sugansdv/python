import re
import os

# 21. Raise ValueError manually if user enters a negative number.
def raise_negative_number():
    print("\n[21] Raise ValueError for negative number:")
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative number not allowed.")
    print("Valid number:", num)

# 22. Raise TypeError if function argument is not a string.
def check_string_type(data):
    print("\n[22] Raise TypeError if argument is not string:")
    if not isinstance(data, str):
        raise TypeError("Input must be a string.")
    print("Valid string:", data)

# 23. Function that only accepts positive integers using raise.
def accept_positive_integer(num):
    print("\n[23] Accept only positive integers:")
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Only positive integers allowed.")
    print("Accepted positive integer:", num)

# 24. Simulate a login system and raise exception if password is incorrect.
def login_system():
    print("\n[24] Login system with password check:")
    correct_password = "admin123"
    password = input("Enter password: ")
    if password != correct_password:
        raise PermissionError("Incorrect password!")
    print("Login successful.")

# 25. Raise an error if a required key is missing from a dictionary.
def check_required_key():
    print("\n[25] Check for required key in dictionary:")
    data = {"name": "John", "age": 25}
    if "email" not in data:
        raise KeyError("Missing required key: 'email'")
    print("Email:", data["email"])

# 26. Raise a ZeroDivisionError with custom error message.
def custom_zero_division():
    print("\n[26] Raise custom ZeroDivisionError:")
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    if b == 0:
        raise ZeroDivisionError("Custom Error: Division by zero is not allowed.")
    print("Result:", a / b)

# 27. Use assert to raise error if number is not even.
def assert_even_number():
    print("\n[27] Assert even number:")
    num = int(input("Enter an even number: "))
    assert num % 2 == 0, "Number is not even."
    print("Valid even number.")

# 28. Validate email format and raise ValueError if invalid.
def validate_email():
    print("\n[28] Validate email format:")
    email = input("Enter your email: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email format.")
    print("Valid email:", email)

# 29. Raise exception if list is empty before processing.
def process_list(lst):
    print("\n[29] Process list after checking for emptiness:")
    if not lst:
        raise Exception("List is empty.")
    print("Processing list:", lst)

# 30. Raise error if file is empty before reading.
def read_nonempty_file():
    print("\n[30] Read file only if not empty:")
    file_path = "checkfile.txt"
    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist.")

    if os.stat(file_path).st_size == 0:
        raise ValueError("File is empty.")
    
    with open(file_path, "r") as f:
        print("File contents:\n", f.read())

# ======================
# Run all examples safely
# ======================
if __name__ == "__main__":
    functions = [
        raise_negative_number,
        lambda: check_string_type("Hello"),          # change to test non-string
        lambda: accept_positive_integer(10),         # change to test invalid
        login_system,
        check_required_key,
        custom_zero_division,
        assert_even_number,
        validate_email,
        lambda: process_list([1, 2, 3]),             # Change to [] to test exception
        read_nonempty_file
    ]

    for func in functions:
        try:
            func()
        except Exception as e:
            print("❌ Exception:", e)
