
print("=======================================")
print("         Login Authentication System         ")
print("=======================================\n")

# Predefined credentials
stored_username = "admin"
stored_password = "pass123"

# Input: Username and Password
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# Use identity operator and if-else for validation
if username_input == stored_username and password_input == stored_password:
    if username_input is stored_username and password_input is stored_password:
        print("\n Login successful (identity check passed)")
    else:
        print("\n Login successful (value matched, but not same identity)")
else:
    if username_input is not stored_username or password_input is not stored_password:
        print("\n Login failed (invalid credentials)")
