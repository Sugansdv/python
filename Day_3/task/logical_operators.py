# 🔐 Logical Operators Tasks (15–20)

# Task 15: Use 'and' to check if age is above 18 and the person has an ID.
print(" Task 15: Check if Age > 18 AND Has ID")
age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower() == "yes"
if age > 18 and has_id:
    print("Entry allowed ")
else:
    print("Entry denied ")

# Task 16: Use 'or' to check if a user entered 'yes' or 'y' as confirmation.
print("\n Task 16: Confirmation Check Using OR")
response = input("Do you agree? (yes/y/no): ").lower()
if response == "yes" or response == "y":
    print("Confirmation accepted ")
else:
    print("Confirmation declined ")

# Task 17: Use 'not' to reverse a comparison result.
print("\n Task 17: Reverse Comparison Using NOT")
num = int(input("Enter a number: "))
if not num > 0:
    print("The number is NOT positive ")
else:
    print("The number is positive ")

# Task 18: Club entry only if age ≥ 21 and dress code is “formal”.
print("\n Task 18: Club Entry Check (Age ≥ 21 AND Dress Code = 'formal')")
age = int(input("Enter your age: "))
dress = input("Enter your dress code (formal/casual): ").lower()
if age >= 21 and dress == "formal":
    print("Access granted to the club 🎉")
else:
    print("Access denied. Age or dress code invalid ")

# Task 19: Ask user two boolean inputs and evaluate them using all logical operators.
print("\n Task 19: Logical Operations on Two Boolean Inputs")
bool1 = input("Enter first value (true/false): ").lower() == "true"
bool2 = input("Enter second value (true/false): ").lower() == "true"
print(f"{bool1} and {bool2} = {bool1 and bool2}")
print(f"{bool1} or {bool2} = {bool1 or bool2}")
print(f"not {bool1} = {not bool1}")
print(f"not {bool2} = {not bool2}")

# Task 20: Combine multiple conditions using and/or and print pass/fail logic.
print("\n Task 20: Pass/Fail Logic Using Multiple Conditions")
marks = int(input("Enter marks out of 100: "))
attendance = int(input("Enter attendance percentage: "))
if marks >= 50 and (attendance >= 75 or marks >= 90):
    print("You Passed ")
else:
    print("You Failed ")
