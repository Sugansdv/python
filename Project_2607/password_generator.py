import random
import string
from cryptography.fernet import Fernet
import os

# ======================
#  ENCRYPTION SETUP
# ======================
KEY_FILE = "secret.key"
PASSWORD_FILE = "passwords.enc"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_passwords(data):
    f = Fernet(load_key())
    encrypted = f.encrypt(data.encode())
    with open(PASSWORD_FILE, "wb") as file:
        file.write(encrypted)
    print(" Passwords saved to encrypted file.")

# ======================
#  PASSWORD GENERATOR
# ======================
def get_password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return " Please select at least one character type!"

    return ''.join(random.choice(characters) for _ in range(length))

# ======================
#  MAIN MENU
# ======================
def main():
    generate_key()
    all_passwords = []

    while True:
        print("""
=====  Password Generator =====
1. Generate Password(s)
2. Save Passwords to Encrypted File
3. Exit
""")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            try:
                count = int(input("How many passwords? "))
                length = int(input("Enter length of each password: "))

                use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
                use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
                use_digits = input("Include numbers? (y/n): ").lower() == 'y'
                use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

                print("\n Generated Passwords:")
                for _ in range(count):
                    pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
                    strength = get_password_strength(pwd)
                    print(f"{pwd}   Strength: {strength}")
                    all_passwords.append(f"{pwd}  ({strength})")
            except ValueError:
                print(" Invalid input. Please enter numeric values.")

        elif choice == '2':
            if not all_passwords:
                print(" No passwords to save.")
            else:
                encrypt_passwords('\n'.join(all_passwords))

        elif choice == '3':
            print(" Exiting.")
            break
        else:
            print(" Invalid option.")

if __name__ == "__main__":
    main()
