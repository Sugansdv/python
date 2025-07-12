# 7. Employee Management System
# Description: Store employee records using nested lists.

# Initial employee records: [Name, ID, Department]
employees = [
    ["Dharun", "E101", "HR"],
    ["Vishwa", "E102", "Sales"],
    ["Sugan", "E103", "IT"]
]

# Function to display all employees
def display_employees():
    print("\nCurrent Employee Records:")
    for index, emp in enumerate(employees, start=1):
        print(f"{index}. Name: {emp[0]}, ID: {emp[1]}, Dept: {emp[2]}")

# Display initial records
display_employees()

# Add a new employee
employees.append(["Anu", "E104", "Finance"])
print("\nAdded new employee: Diana")

# Update employee department (update Charlie's department to 'Development')
for emp in employees:
    if emp[0] == "Sugan":
        emp[2] = "Development"
        print("Updated Charlie's department to Development.")

# Remove an employee (remove Bob)
for emp in employees:
    if emp[0] == "Vishwa":
        employees.remove(emp)
        print("Removed employee: Bob")
        break

# Access employee by index (2nd employee in the list)
if len(employees) >= 2:
    print("\nAccessed by index - 2nd employee:", employees[1])

# Sort employees alphabetically by name
employees.sort(key=lambda x: x[0])
print("\nEmployees sorted alphabetically by name.")

# Final display
display_employees()
