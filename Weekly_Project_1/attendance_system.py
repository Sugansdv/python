# Student Attendance System

# Input: list of student names
input_names = input("Enter student names (comma-separated): ")
students = [name.strip().title() for name in input_names.split(",")]

# Input: attendance status ("P" or "A") for each student
attendance = []
for name in students:
    status = input(f"Is {name} present? (P/A): ").strip().upper()
    attendance.append((name, status))

# Use for loop to count how many are present
present_count = 0
for _, status in attendance:
    if status == "P":
        present_count += 1

# Print summary
print("\n======= Attendance Summary =======")
for name, status in attendance:
    print(f"{name}: {'Present' if status == 'P' else 'Absent'}")
print(f"\nTotal Present: {present_count}")
print(f"Total Absent : {len(students) - present_count}")
print("==================================")
