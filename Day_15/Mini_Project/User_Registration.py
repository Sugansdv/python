# user_registration.py

import re
import logging

# Setup logging
logging.basicConfig(filename='registration_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom Exceptions
class InvalidNameError(Exception): pass
class InvalidEmailError(Exception): pass
class InvalidPasswordError(Exception): pass

def validate_name(name):
    if not name.isalpha() or len(name) < 3:
        raise InvalidNameError("Name must be at least 3 alphabetic characters.")

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, email):
        raise InvalidEmailError("Email format is invalid.")

def validate_password(password):
    if len(password) < 6:
        raise InvalidPasswordError("Password must be at least 6 characters.")
    if not any(char.isdigit() for char in password):
        raise InvalidPasswordError("Password must contain at least one number.")
    if not any(char.isalpha() for char in password):
        raise InvalidPasswordError("Password must contain at least one letter.")

def register_user():
    try:
        name = input("Enter your name: ")
        validate_name(name)

        email = input("Enter your email: ")
        validate_email(email)

        password = input("Enter a password: ")
        validate_password(password)

    except (InvalidNameError, InvalidEmailError, InvalidPasswordError) as e:
        print(f"❌ Registration failed: {e}")
        logging.error("ValidationError: %s", e)
    else:
        print(f"✅ Registration successful! Welcome, {name}")
    finally:
        print("🔚 Registration process complete.")

# Run the registration
if __name__ == "__main__":
    register_user()
