# 4. Simple Login System
# Objective: Allow login until correct password is entered.

correct_password = "admin123"

# • Use while True for infinite loop.
while True:
    # • Ask user for password input.
    user_input = input("Enter password: ")

    # • Use pass as placeholder for future logging.
    pass 

    # • Break if correct password entered.
    if user_input == correct_password:
        print(" Login successful!")
        break
    else:
        print(" Incorrect password. Try again.")
