#2. User Registration & Login System
users = [] 

def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    users.append({"username": username, "password": password}) 
    print("Registration successful.\n")

def login():
    attempts = 3
    while attempts > 0:  
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful.\n")
                return True
        attempts -= 1
        print(f"Incorrect credentials. Attempts left: {attempts}")
    print("Too many failed attempts.\n")
    return False

def show_users():
    print("\n--- Registered Users ---")
    for user in users:
        print(f"Username: {user['username']}")
    print()

while True:
    print("1. Register")
    print("2. Login")
    print("3. Show Users")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        show_users()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")
