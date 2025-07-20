def register_user(users):
    username = input("Enter new username: ").strip()
    if username in users:
        print("Username already exists.")
    else:
        users.add(username)
        print(f"User '{username}' registered successfully.")
