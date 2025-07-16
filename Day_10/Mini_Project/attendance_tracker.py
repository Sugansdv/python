# 11. School Attendance Tracker
# Description: Manage student attendance per day.
# Requirements:
# - Structure: {date: [student_names_present]}
# - Add attendance for each day
# - Mark absentees
# - Use .keys() to get all dates
# - Reverse query: for a student, show attendance count

attendance = {
    "2025-07-01": ["Alice", "Bob", "Charlie"],
    "2025-07-02": ["Alice", "Charlie"],
    "2025-07-03": ["Bob", "David"]
}

def add_attendance(date, students_present):
    attendance[date] = students_present
    print(f"Attendance added for {date}.")

def mark_absentees(date, all_students):
    present = attendance.get(date, [])
    absent = [student for student in all_students if student not in present]
    print(f"\nAbsentees on {date}: {', '.join(absent) if absent else 'None'}")

def list_all_dates():
    print("\nDates with attendance records:")
    for date in attendance.keys():
        print(date)

def student_attendance_count(student_name):
    count = sum(1 for day in attendance.values() if student_name in day)
    print(f"\n{student_name} was present on {count} day(s).")

add_attendance("2025-07-04", ["Alice", "David"])
mark_absentees("2025-07-04", ["Alice", "Bob", "Charlie", "David"])
list_all_dates()
student_attendance_count("Alice")
student_attendance_count("Bob")
