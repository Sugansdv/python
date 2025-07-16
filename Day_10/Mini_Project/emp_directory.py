
# 3. Employee Directory System
# Description: Maintain employee records.
# Requirements:
# - Use nested dictionary: {emp_id: {"name": ..., "dept": ..., "salary": ...}}
# - Add new employee
# - Update salary or department
# - Delete employee using pop()
# - Search employees by department
# - Use setdefault() to prevent overwriting existing records

employees = {
    101: {"name": "Alice", "dept": "HR", "salary": 50000},
    102: {"name": "Bob", "dept": "IT", "salary": 60000}
}

def add_employee(emp_id, name, dept, salary):
    employees.setdefault(emp_id, {"name": name, "dept": dept, "salary": salary})

def update_employee(emp_id, field, value):
    if emp_id in employees:
        employees[emp_id][field] = value

def delete_employee(emp_id):
    employees.pop(emp_id, None)

def search_by_department(dept):
    return {eid: info for eid, info in employees.items() if info["dept"] == dept}
