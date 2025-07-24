# === Custom Exceptions ===

# 31. NegativeNumberError
class NegativeNumberError(Exception):
    pass

def check_positive_custom(n):
    if n < 0:
        raise NegativeNumberError("Negative number not allowed.")
    print("Positive number:", n)

# 32. InvalidAgeError
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    print("Valid age:", age)

# 33. InsufficientFundsError
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds.")
    print(f"Withdrawn {amount}. Remaining balance: {balance - amount}")

# 34. GradeOutOfRangeError
class GradeOutOfRangeError(Exception):
    pass

def assign_grade(marks):
    if marks < 0 or marks > 100:
        raise GradeOutOfRangeError("Marks must be between 0 and 100.")
    print("Grade assigned for marks:", marks)

# 35. UnauthorizedAccessError
class UnauthorizedAccessError(Exception):
    pass

def access_resource(role):
    if role != "admin":
        raise UnauthorizedAccessError("Only admin can access this resource.")
    print("Access granted.")

# 36. InvalidFileFormatError
class InvalidFileFormatError(Exception):
    pass

def upload_file(filename):
    if not filename.endswith((".jpg", ".png", ".pdf")):
        raise InvalidFileFormatError("Unsupported file format.")
    print("File uploaded:", filename)

# 37. LoginAttemptsExceeded
class LoginAttemptsExceeded(Exception):
    pass

def login_system(attempts):
    if attempts > 3:
        raise LoginAttemptsExceeded("Too many failed login attempts.")
    print("Login successful or attempt recorded.")

# 38. ObjectStateError
class ObjectStateError(Exception):
    pass

class Door:
    def __init__(self):
        self.state = "closed"

    def open(self):
        if self.state == "open":
            raise ObjectStateError("Door is already open.")
        self.state = "open"
        print("Door opened.")

# 39. FileTooLargeError
class FileTooLargeError(Exception):
    pass

def validate_file_size(size_mb):
    if size_mb > 10:
        raise FileTooLargeError("File too large. Must be <= 10MB.")
    print("File size is acceptable.")

# 40. BelowAbsoluteZeroError
class BelowAbsoluteZeroError(Exception):
    pass

def convert_to_kelvin(celsius):
    if celsius < -273.15:
        raise BelowAbsoluteZeroError("Temperature cannot be below absolute zero.")
    print(f"Kelvin: {celsius + 273.15}")

# === Run All tasks ===
if __name__ == "__main__":
    try:
        check_positive_custom(5)
        validate_age(25)
        withdraw(1000, 500)
        assign_grade(85)
        access_resource("admin")
        upload_file("document.pdf")
        login_system(2)
        door = Door()
        door.open()
        validate_file_size(5)
        convert_to_kelvin(-100)
    except Exception as e:
        print("Caught Exception:", e)
