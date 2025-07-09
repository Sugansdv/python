#  10. User Info Collector
# Objective: Collect 5 names and ages.

user_info = {}
count = 0

# • Use while loop to input names and ages.
while count < 5:
    name = input(f"Enter name of user {count + 1}: ").strip()

    # • Skip if name is blank using continue.
    if name == "":
        print(" Name cannot be blank. Try again.")
        continue

    try:
        age = int(input(f"Enter age of {name}: "))
    except ValueError:
        print(" Invalid age. Try again.")
        continue

    # • Use pass in future placeholder for email validation.
    pass  

    # • Store data in a dictionary.
    user_info[name] = age
    count += 1

# Display collected user info
print("\n Collected User Information:")
for name, age in user_info.items():
    print(f"👤 {name} - {age} years old")
