# ==== MINI PROJECT 10: SIMPLE LOGIN ATTEMPT COUNTER ====

print("====================")
print("Simple Login Attempt Counter")
print("====================")

# Set correct credentials
correct_username = "admin"
correct_password = "1234"

# Use a for loop with range(3) for 3 attempts
for attempt in range(3):
    # Ask for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Use if to check; if correct, break loop
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect credentials. Try again.\n")
else:
    # If 3 wrong attempts, print “Account Locked”
    print("Account Locked. Too many failed attempts.")
