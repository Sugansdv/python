# Voting Eligibility Checker

# Input list of ages
input_str = input("Enter the ages (comma-separated): ")
age_list = [int(age.strip()) for age in input_str.split(",")]

# Use for loop and condition to print who is eligible (age ≥ 18)
print("\n======= Voting Eligibility Result =======")
for i, age in enumerate(age_list, start=1):
    if age >= 18:
        print(f"Person {i} (Age {age}): Eligible to vote")
    else:
        print(f"Person {i} (Age {age}): Not eligible to vote")
print("=========================================")
