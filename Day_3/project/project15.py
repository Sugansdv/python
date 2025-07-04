
print("=======================================")
print("         Bitwise Access Rights Checker         ")
print("=======================================\n")

# Define permission constants
READ = 1       
WRITE = 2    
EXECUTE = 4   

# Input: user's combined permission code
permission_code = int(input("Enter user permission code (e.g., 3 for Read+Write): "))

# Display permission breakdown using bitwise AND &
print("\n========== Access Rights ==========")
print(f"Permission Code : {permission_code}")
print(f"Read Access     : {' Yes' if permission_code & READ else ' No'}")
print(f"Write Access    : {' Yes' if permission_code & WRITE else ' No'}")
print(f"Execute Access  : {' Yes' if permission_code & EXECUTE else ' No'}")
print("=====================================")
