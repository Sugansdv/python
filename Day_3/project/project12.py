
print("=======================================")
print("       Driving License Eligibility System       ")
print("=======================================\n")

# Input: age and Aadhar possession status
age = int(input("Enter your age: "))
has_aadhar = input("Do you have an Aadhar card? (yes/no): ").lower()

#Use if and nested if to validate.
#Use logical, identity, and assignment operators.
if age >= 18:  
    if has_aadhar == "yes":  
        eligible = True  
        print("\n You are eligible to apply for a Driving License.")
    elif has_aadhar is not "yes":  
        eligible = False
        print("\n You must have an Aadhar card to apply.")
else:
    eligible = False
    print("\n You must be at least 18 years old to apply.")

print("=======================================")
print(f"\nEligibility status: {eligible}")
print("=======================================")
