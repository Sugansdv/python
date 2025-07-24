import shutil
import logging

# ===== Task 46: Calculator =====
def calculator():
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a / b
        else:
            raise ValueError("Invalid operator.")

        print("Result:", result)
    except ValueError as ve:
        print("Input error:", ve)
    except ZeroDivisionError as ze:
        print("Math error:", ze)


# ===== Task 47: File Copy Tool =====
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except IsADirectoryError:
        print("Error: Source is a directory, not a file.")
    except Exception as e:
        print("Unexpected error:", e)


# ===== Task 48: User Registration =====
class InvalidFieldError(Exception):
    pass

def register_user(name, email, password):
    if not name.strip():
        raise InvalidFieldError("Name cannot be empty.")
    if '@' not in email or '.' not in email:
        raise InvalidFieldError("Invalid email format.")
    if len(password) < 6:
        raise InvalidFieldError("Password must be at least 6 characters.")
    print("User registered successfully!")


# ===== Task 49: Logging Exceptions =====
logging.basicConfig(filename='app_errors.log', level=logging.ERROR)

def divide_and_log(a, b):
    try:
        return a / b
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        print("An error occurred. Check log file.")


# ===== Task 50: Payment Gateway =====
class PaymentError(Exception):
    pass

def process_payment(card_number, amount):
    try:
        if len(str(card_number)) != 16:
            raise PaymentError("Invalid card number.")
        if amount <= 0:
            raise PaymentError("Amount must be greater than 0.")
        print(f"Payment of ₹{amount} processed for card ending with {str(card_number)[-4:]}")
    except PaymentError as e:
        print("Payment failed:", e)
    except Exception as e:
        print("Unexpected error:", e)


# ===== Run  Tasks =====
if __name__ == "__main__":
    print("\n--- Task 46: Calculator ---")
    calculator()

    print("\n--- Task 47: File Copy Tool ---")
    copy_file("source.txt", "backup.txt") 

    print("\n--- Task 48: User Registration ---")
    try:
        register_user("Alice", "alice@example.com", "mypassword")
    except InvalidFieldError as e:
        print("Registration error:", e)

    print("\n--- Task 49: Log Exception to File ---")
    divide_and_log(10, 0)  # This logs ZeroDivisionError to app_errors.log

    print("\n--- Task 50: Payment Gateway ---")
    process_payment(1234567812345678, 500)
