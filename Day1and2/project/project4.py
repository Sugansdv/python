## 4. Personal Greeting App
print("========================================")
print("           Personal Greeting App        ")
print("========================================")
# 1. Ask the user for their name and favorite hobby
name = input("Enter your name: ")
hobby = input("Enter your favorite hobby: ")

# 2. Print a personalized greeting using f-strings
print(f"\nHi {name}! It's great that you enjoy {hobby}.")

# 3. Confirm the type of each input
print(f"\nType of 'name': {type(name)}")
print(f"Type of 'hobby': {type(hobby)}")
