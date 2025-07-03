## 14. Voting Eligibility Checker
print("========================================")
print("         Voting Eligibility Checker      ")
print("========================================")

# Ask for age (input)
age = int(input("Enter your age: "))

# Print whether the user is eligible to vote
if age >= 18:
    print(" You are eligible to vote.")
else:
    print(" You are not eligible to vote yet.")

# Show the type of the age variable
print(f"Type of 'age' variable: {type(age)}")
