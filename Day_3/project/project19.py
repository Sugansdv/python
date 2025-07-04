
print("=======================================")
print("           Mobile Recharge Validator           ")
print("=======================================\n")

# Input: mobile number and recharge amount
mobile = input("Enter your 10-digit mobile number: ")
amount = float(input("Enter recharge amount (₹): "))

# Validation using len(), logical and comparison operators
if len(mobile) == 10 and mobile.isdigit():
    if amount > 10:
        print(f"\n Recharge of ₹{amount} for {mobile} successful.")
    else:
        print("\n Recharge amount must be more than ₹10.")
else:
    print("\n Invalid mobile number. Please enter a 10-digit numeric value.")
