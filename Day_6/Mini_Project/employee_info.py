#  7. Employee Info Manager

# Store all employee data
employees = []

# • Accept name, role, salary using **kwargs
def add_employee(**kwargs):
    employees.append(kwargs)
    # • Display formatted info using f-string
    print(f"Employee Added: {kwargs['name']} - {kwargs['role']} - ₹{kwargs['salary']}")

# • Return dictionary of all employees
def get_all_employees():
    return employees

add_employee(name="Dharun", role="Developer", salary=50000)
add_employee(name="Vishwa", role="Designer", salary=45000)
print("All Employees:", get_all_employees())
