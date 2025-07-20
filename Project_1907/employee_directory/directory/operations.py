def add_employee(employees, emp_id_tuple, name, department):
    for emp in employees:
        if emp['id'][0] == emp_id_tuple[0]:
            print("Employee ID already exists.")
            return
    employees.append({
        "id": emp_id_tuple,
        "name": name,
        "department": department
    })
    print("Employee added successfully.")

def remove_employee(employees, emp_id):
    for emp in employees:
        if emp['id'][0] == emp_id:
            employees.remove(emp)
            print("Employee removed.")
            return
    print("Employee not found.")

def update_employee(employees, emp_id, name, department):
    for emp in employees:
        if emp['id'][0] == emp_id:
            emp['name'] = name
            emp['department'] = department
            print("Employee updated.")
            return
    print("Employee not found.")
