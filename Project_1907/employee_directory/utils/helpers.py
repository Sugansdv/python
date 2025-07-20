def list_departments(employees):
    departments = {emp['department'] for emp in employees}
    print("Departments:")
    for d in sorted(departments):
        print("-", d)
