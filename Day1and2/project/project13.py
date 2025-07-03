## 13. Profile Builder

print("========================================")
print("             Profile Builder            ")
print("========================================")

# 1. Ask for name, age, and city
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# 2. Store in a dictionary
profile = {
    "Name": name,
    "Age": age,
    "City": city
}

# 3. Print a formatted profile summary using f-strings
print("\n Profile Summary:")
print(f"Name : {profile['Name']}")
print(f"Age  : {profile['Age']}")
print(f"City : {profile['City']}")
