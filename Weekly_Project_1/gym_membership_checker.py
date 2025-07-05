# Gym Membership Checker

# Variables: name, age, BMI
name = "Dharun Vishwa"
age = 22
bmi = 23.5

# Use if:
# If age > 18 and BMI < 25 → Eligible
# Else → Not Eligible
if age > 18 and bmi < 25:
    eligibility = "Eligible for Gym Membership Offers"
else:
    eligibility = "Not Eligible for Gym Membership Offers"

# Display formatted output
print("\n====== Gym Membership Checker ======")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"BMI        : {bmi}")
print(f"Eligibility: {eligibility}")
print("====================================")
