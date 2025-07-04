
print("=======================================")
print("      Salary Tax Deduction Calculator   ")
print("=======================================\n")

# Input: base salary
salary = float(input("Enter your base annual salary (in ₹): "))

# Initialize tax and net salary using assignment operator
tax = 0
net_salary = salary

# Tax calculation using if-elif-else and arithmetic
if salary < 500000:
    tax = 0
elif salary <= 1000000:
    tax = salary * 0.10
else:
    tax = salary * 0.20

# Deduct tax using assignment operator
net_salary -= tax

# Formatted output
print("\n========== Salary Summary ==========")
print(f"Base Salary     : ₹{salary:,.2f}")
print(f"Tax Deducted    : ₹{tax:,.2f}")
print(f"Net Salary      : ₹{net_salary:,.2f}")
print("=====================================")
