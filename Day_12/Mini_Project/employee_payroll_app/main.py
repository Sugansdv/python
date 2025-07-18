from payroll.employee import Employee
from payroll.payslip import generate_payslip

if __name__ == "__main__":
    print("=== Employee Payroll System ===")
    emp = Employee(emp_id=1001, name="John Doe", designation="Software Engineer", join_date="2018-06-15")
    
    basic_salary = 40000
    hra = 10000
    bonus = 5000

    payslip = generate_payslip(emp, basic_salary, hra, bonus)
    print(payslip)
