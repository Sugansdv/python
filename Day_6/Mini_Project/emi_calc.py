#18. Loan EMI Calculator
# • Input principal, rate, time
principal = float(input("Enter loan amount (principal): "))
rate = float(input("Enter annual interest rate (in %): "))
time = int(input("Enter loan duration (in years): "))

# • Use EMI formula in function
def calculate_emi(p, r, t):
    monthly_rate = r / (12 * 100)  # converting annual rate to monthly decimal
    months = t * 12
    # • Bonus: use lambda to shorten logic
    emi_formula = lambda p, r, n: (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    emi = emi_formula(p, monthly_rate, months)
    return round(emi, 2)

emi = calculate_emi(principal, rate, time)
print(f"\nYour monthly EMI is: ₹{emi}")
