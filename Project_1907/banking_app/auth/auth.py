def login(users):
    username = input("Enter username: ").strip()
    if username in users:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("User not found.")
        return None
