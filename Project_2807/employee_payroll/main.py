from core.payroll import PayrollSystem

def main():
    ps = PayrollSystem()
    
    ps.add_employee("E001", "Alice", 45, 25)
    ps.add_employee("E002", "Bob", 38, 20)
    ps.add_employee("E003", "Charlie", 50, 30)

    print("\n--- Payslips ---")
    ps.generate_payslips()

    print("\n--- Overtime Employees ---")
    for emp in ps.overtime_generator():
        print(emp)

    ps.export_to_csv()

    print("\n--- Admin Update (Fail) ---")
    ps.update_salary("E002", 42, 22)  # should fail

    print("\n--- Admin Update (Success) ---")
    ps.update_salary("E002", 42, 22, is_admin=True)

    print("\n--- Updated Payslips ---")
    ps.generate_payslips()

if __name__ == "__main__":
    from core.employee import Employee  # Required to avoid circular import
    main()
