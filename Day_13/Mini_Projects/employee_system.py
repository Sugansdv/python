# ----------------- Base Class -----------------
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        return 0

# ----------------- Derived Classes -----------------
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, daily_rate, days_worked):
        super().__init__(emp_id, name)
        self.daily_rate = daily_rate
        self.days_worked = days_worked

    def calculate_salary(self):
        gross = self.daily_rate * self.days_worked
        return gross

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        gross = self.hourly_rate * self.hours_worked
        return gross

# ----------------- Payroll Utility -----------------
class Payroll:
    @staticmethod
    def calculate_tax(salary):
        return salary * 0.1 if salary > 5000 else 0  # 10% tax if salary > ₹5000

    def generate_pay_slip(self, employee):
        gross = employee.calculate_salary()
        tax = self.calculate_tax(gross)
        net = gross - tax
        print(f"\n Pay Slip for {employee.name} (ID: {employee.emp_id})")
        print(f"Gross Salary: ₹{gross}")
        print(f"Tax Deducted: ₹{tax}")
        print(f"Net Salary: ₹{net}")
        print("-----------------------------")

# ----------------- Test Flow -----------------
if __name__ == "__main__":
    emp1 = FullTimeEmployee(101, "Anita", daily_rate=1000, days_worked=22)
    emp2 = PartTimeEmployee(102, "Ravi", hourly_rate=150, hours_worked=30)

    payroll = Payroll()
    payroll.generate_pay_slip(emp1)
    payroll.generate_pay_slip(emp2)
