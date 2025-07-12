# 10. Email Validation Program
# Concepts: string checks, while, functions.
# • Ask user to enter valid email.
# • Check for @, ., and min length.
# • Loop until a valid email is entered.
# • Use find(), split(), etc.

def is_valid_email(email):
    if len(email) < 6:
        return False
    if "@" not in email or "." not in email:
        return False
    at_pos = email.find("@")
    dot_pos = email.rfind(".")
    if at_pos < 1 or dot_pos < at_pos + 2 or dot_pos == len(email) - 1:
        return False
    return True

while True:
    email = input("Enter a valid email address: ")
    if is_valid_email(email):
        print("Valid email entered.")
        break
    else:
        print("Invalid email. Please try again.\n")
