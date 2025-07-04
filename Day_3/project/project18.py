
print("=======================================")
print("         Movie Ticket Price Calculator        ")
print("=======================================\n")

# Input: age of the customer
age = int(input("Enter your age: "))

# Determine ticket price using if-elif-else
if age < 12:
    price = 50
    category = "Child"
elif age <= 60:
    price = 120
    category = "Adult"
else:
    price = 100
    category = "Senior"

print("\n========== Ticket Summary ==========")
print(f"Age Group   : {category}")
print(f"Ticket Price: ₹{price}")
print("=====================================")
