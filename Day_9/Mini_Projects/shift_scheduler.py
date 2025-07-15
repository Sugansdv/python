# 13. Employee Shift Scheduler
# Goal: Schedule employee work shifts.
# Requirements:
# • Store each shift as (employee_id, name, (start_time, end_time))
# • Access specific timings using nested indexing.
# • Use slicing to show first 5 employees.
# • Iterate and unpack for payroll calculations.

# List of employee shifts
shifts = [
    (101, "Alice", ("09:00", "17:00")),
    (102, "Bob", ("08:30", "16:30")),
    (103, "Charlie", ("10:00", "18:00")),
    (104, "David", ("09:30", "17:30")),
    (105, "Eva", ("08:00", "16:00")),
    (106, "Frank", ("11:00", "19:00")),
    (107, "Grace", ("07:00", "15:00"))
]

# Show first 5 employees
print(" First 5 Employee Shifts:\n")
for emp_id, name, (start, end) in shifts[:5]:
    print(f"ID: {emp_id}, Name: {name}, Shift: {start} to {end}")

# Access a specific shift time directly
third_shift_end = shifts[2][2][1]
print(f"\n Charlie's shift ends at: {third_shift_end}")

# Iterate and unpack for payroll (assuming 8-hour shifts)
print("\n Shift Summary:\n")
for emp_id, name, (start, end) in shifts:
    print(f"{emp_id} - {name} → Shift: {start} to {end} (8 hrs)")
