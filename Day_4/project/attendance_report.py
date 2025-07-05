# ==== MINI PROJECT 6: ATTENDANCE REPORT GENERATOR ====

print("====================")
print("Attendance Report Generator")
print("====================")

# Input: list of names
names_input = input("Enter student names separated by commas: ")
students = [name.strip().title() for name in names_input.split(',')]

# Output: numbered list with status "Present"
# Use for loop + enumerate() with start=101
print("\nAttendance Report:")
for roll_no, name in enumerate(students, start=101):
    print(f"{roll_no}. {name} - Present")
