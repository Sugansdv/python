from datetime import datetime

def generate_payslip(employee, basic, hra, bonus=0):
    from .salary import calculate_gross_salary, calculate_net_salary
    from .tax import calculate_tax

    gross = calculate_gross_salary(basic, hra, bonus)
    tax = calculate_tax(gross)
    net = calculate_net_salary(gross, tax)

    return f"""
    ===============================
             PAYSLIP
    ===============================
    Employee ID   : {employee.emp_id}
    Name          : {employee.name}
    Designation   : {employee.designation}
    Join Date     : {employee.join_date}
    Experience    : {employee.get_experience()} years

     Salary Details:
    -------------------------------
    Basic Salary  : ₹{basic}
    HRA           : ₹{hra}
    Bonus         : ₹{bonus}
    -------------------------------
    Gross Salary  : ₹{gross}
    Tax Deducted  : ₹{tax}
    Net Salary    : ₹{net}

    Generated On  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    ===============================
    """
