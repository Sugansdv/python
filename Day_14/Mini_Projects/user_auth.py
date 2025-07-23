import hashlib
import os
from datetime import datetime

USER_FILE = "users.txt"
LOG_FILE = "login_logs.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()

    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            for line in f:
                stored_user = line.strip().split(":")[0]
                if username == stored_user:
                    print(" Username already exists.")
                    return

    hashed_pw = hash_password(password)
    with open(USER_FILE, 'a') as f:
        f.write(f"{username}:{hashed_pw}\n")
    print(" Signup successful!")

def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    hashed_pw = hash_password(password)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    success = False
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            for line in f:
                stored_user, stored_hash = line.strip().split(":")
                if username == stored_user and hashed_pw == stored_hash:
                    success = True
                    break

    with open(LOG_FILE, 'a') as log:
        log.write(f"[{timestamp}] LOGIN {'SUCCESS' if success else 'FAIL'} for user '{username}'\n")

    if success:
        print(" Login successful!")
    else:
        print(" Invalid username or password.")

def main():
    while True:
        print("\n User Auth System")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print(" Exiting system.")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
