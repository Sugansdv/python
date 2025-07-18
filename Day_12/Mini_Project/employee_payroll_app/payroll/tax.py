import math

def calculate_tax(gross_salary):
    if gross_salary <= 25000:
        return 0
    elif gross_salary <= 50000:
        return math.floor(gross_salary * 0.10)
    elif gross_salary <= 100000:
        return math.floor(gross_salary * 0.20)
    else:
        return math.floor(gross_salary * 0.30)
