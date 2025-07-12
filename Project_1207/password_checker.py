# 5. Password Strength Checker
# Concepts: strings, functions, while loop.
# • Ask for password repeatedly until it meets criteria.
# • Must include lowercase, uppercase, digit, and symbol.
# • Use any() and string methods.
# • Function to evaluate and return strength status.

import string

def check_strength(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    if all([has_lower, has_upper, has_digit, has_symbol]):
        return "Strong"
    else:
        return "Weak"

while True:
    pwd = input("Enter a password: ")
    result = check_strength(pwd)
    print(f"Password Strength: {result}")
    if result == "Strong":
        break
    else:
        print("Password must include lowercase, uppercase, digit, and symbol.\n")
