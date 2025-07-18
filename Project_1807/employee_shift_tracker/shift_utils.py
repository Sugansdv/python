

from data.shift_data import employee_shifts, assigned_shifts

def assign_shift(emp_id, name, shift):
    if shift in assigned_shifts:
        print(f" Shift '{shift}' already assigned.")
        return
    employee_shifts[emp_id] = {
        "name": name,
        "shift": shift
    }
    assigned_shifts.add(shift)
    print(f"Assigned shift '{shift}' to {name} (ID: {emp_id[0]}).")

def view_all_shifts():
    if not employee_shifts:
        print("No shifts assigned yet.")
        return
    print("\n Assigned Shifts:")
    for emp_id, info in employee_shifts.items():
        print(f"ID: {emp_id[0]} | Name: {info['name']} | Shift: {info['shift']}")
