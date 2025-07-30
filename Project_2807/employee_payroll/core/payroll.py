import csv
from core.decorators import admin_only
from core.employee import Employee


class PayrollSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, hours, rate):
        try:
            self.employees[emp_id] = Employee(emp_id, name, hours, rate)
            print(f"Added employee {name}")
        except ValueError as e:
            print(f"Error: {e}")

    def generate_payslips(self):
        for emp in self.employees.values():
            net, tax = emp.calculate_salary()
            print(f"{emp.name} | Net Salary: ${net:.2f} | Tax: ${tax:.2f}")

    @admin_only
    def update_salary(self, emp_id, hours, rate, is_admin=False):
        if emp_id in self.employees:
            try:
                self.employees[emp_id].hours = hours
                self.employees[emp_id].rate = rate
                print(f"Updated salary for {self.employees[emp_id].name}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Employee not found.")

    def export_to_csv(self, filename="payroll.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Hours", "Rate", "Net Salary", "Tax"])
            for emp in self.employees.values():
                net, tax = emp.calculate_salary()
                writer.writerow([emp.emp_id, emp.name, emp.hours, emp.rate, f"{net:.2f}", f"{tax:.2f}"])
        print(f"Payroll exported to {filename}")

    def overtime_generator(self):
        return (emp for emp in self.employees.values() if emp.hours > 40)
