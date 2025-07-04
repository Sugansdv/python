
print("=======================================")
print("        User Age Classification System        ")
print("=======================================\n")

# Input: name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Classification using if-elif-else 
# logical and comparison operators
if age < 13:
    category = "Child"
elif age >= 13 and age <= 19: 
    category = "Teenager"
elif age >= 20 and age <= 59:
    category = "Adult"
else:
    category = "Senior"

print("\n========== Age Group Result ==========")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Category   : {category}")
print("=======================================")
