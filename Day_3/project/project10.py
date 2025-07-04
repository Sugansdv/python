
print("=======================================")
print("         Access Control Based on Role         ")
print("=======================================\n")

# Input: role and ID status
role = input("Enter your role (admin/user): ").lower()
has_id = input("Do you have your ID? (yes/no): ").lower()

# Use nested if and logical/membership operators
if role in ["admin", "user"]:  # membership operator
    if has_id == "yes":
        if role == "admin":
            print("\n Access granted: Full Admin Privileges.")
        elif role == "user":
            print("\n Access granted: Limited User Access.")
    else:
        print("\n Access Denied: ID is required.")
else:
    print("\n Invalid role. Access Denied.")

# Use `not` 
if not has_id == "yes":
    print(" Access restricted without valid ID.")
