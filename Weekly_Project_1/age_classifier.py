# Age Group Classifier

# Input: age (int)
age = int(input("Enter the person's age: "))

# Use if-elif-else to classify age group
# <13: Child, 13–19: Teen, 20–59: Adult, 60+: Senior
if age < 13:
    group = "Child"
elif 13 <= age <= 19:
    group = "Teen"
elif 20 <= age <= 59:
    group = "Adult"
else:
    group = "Senior"

# Display the result
print("\n========= Age Group Result =========")
print(f"Age          : {age}")
print(f"Age Category : {group}")
print("====================================")
