#  7. Password Strength Tester
# Objective: Validate if password is long enough.

# • Use infinite loop to ask for input.
while True:
    password = input("Enter a password (minimum 6 characters): ")

    # • If password length < 6, use continue to re-prompt.
    if len(password) < 6:
        print(" Password too short. Try again.")
        continue

    # • Use break once it meets conditions.
    break

# • Use else to print "Password accepted".
else:
    print(" Unexpected exit.")  

print(" Password accepted.")
