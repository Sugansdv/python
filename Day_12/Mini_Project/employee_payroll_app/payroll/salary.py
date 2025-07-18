def calculate_gross_salary(basic, hra, bonus=0):
    return basic + hra + bonus

def calculate_net_salary(gross_salary, tax_amount):
    return gross_salary - tax_amount
