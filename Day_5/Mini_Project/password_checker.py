#  2. Password Checker with Limited Attempts
# Objective: Check password input with a maximum of 3 tries.

correct_password = "secure123"
attempts = 0

# • Use while loop with attempts counter.
while attempts < 3:
    user_input = input("Enter password: ")

    # • Use break to exit if password is correct.
    if user_input == correct_password:
        print(" Access granted!")
        break
    else:
        print(" Incorrect password.")
        attempts += 1

# • After the loop, use else to say “Too many attempts!” if not successful.
else:
    print(" Too many attempts!")
