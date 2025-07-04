print("========================================")
print("    Online Voting Eligibility Checker    ")
print("========================================\n")

# Input: Name, Age, Citizenship
name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship (e.g., Indian): ")

# Show data types using type()
print(f"\nData Types → Name: {type(name)}, Age: {type(age)}, Citizenship: {type(citizenship)}\n")

# Eligibility check using comparison and logical operators
if age >= 18 and citizenship.lower() == "indian":
    print(f" Hello {name}, you are eligible to vote in India.")
else:
    print(f" Sorry {name}, you are not eligible to vote in India.")
