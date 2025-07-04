print("=======================================")
print("        Age and Income Loan Checker         ")
print("=======================================\n")

# Input: age and income
age = int(input("Enter your age: "))
income = float(input("Enter your monthly income (₹): "))

# Loan eligibility check
if age < 21:
    status = " Not eligible: Minimum age is 21."
elif income < 20000:
    status = " Not eligible: Minimum income is ₹20,000."
else:
    status = " Eligible for the loan."

# Formatted output
print("\n========== Loan Eligibility Result ==========")
print(f"Age           : {age}")
print(f"Income (₹)    : {income:,.2f}")
print(f"Loan Status   : {status}")
print("=============================================")