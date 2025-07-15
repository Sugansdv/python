# 6. Classroom Attendance Register
# Goal: Record daily student attendance using tuples.
# Requirements:
# • Store attendance as (date, (student1, student2, ...))
# • Use nested tuples for student grouping.
# • Access a specific day's attendance using slicing.
# • Count how many days a student was present using .count().
# • Use tuple unpacking to get date and students.

# List of attendance records
attendance_log = [
    ("2025-07-01", ("Alice", "Bob", "Charlie")),
    ("2025-07-02", ("Alice", "David")),
    ("2025-07-03", ("Bob", "Charlie", "Eva")),
    ("2025-07-04", ("Alice", "Bob", "Eva")),
    ("2025-07-05", ("Charlie", "David", "Eva"))
]

# Access specific day's attendance (e.g., last 2 days)
print(" Last 2 Days' Attendance:\n")
for date, students in attendance_log[-2:]:
    print(f"{date}: {', '.join(students)}")

# Count how many days a student was present
target_student = "Alice"
days_present = sum(target_student in students for _, students in attendance_log)
print(f"\n {target_student} was present on {days_present} day(s).")

# Full attendance report
print("\n Full Attendance Register:")
for date, students in attendance_log:
    print(f"{date} → {', '.join(students)}")
