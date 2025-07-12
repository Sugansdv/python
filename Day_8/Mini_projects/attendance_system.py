# 15. Class Attendance System
# Description: Maintain daily attendance.

# Master list of all students
master_list = ["Arun", "Dharun", "Farah", "Hema", "Sugan", "Vishwa"]

# Store present student names (with accidental duplicates)
present_list = ["Arun", "Dharun", "Arun", "Farah", "Farah"]

# Remove duplicates using set, then convert back to list if needed
present_unique = list(set(present_list))
print("Present Students (duplicates removed):", present_unique)

# Count absentees by comparing with master list
absentees = []
for student in master_list:
    if student not in present_unique:
        absentees.append(student)

# Display attendance summary
print(f"\n Total Students: {len(master_list)}")
print(f"Present: {len(present_unique)}")
print(f" Absent: {len(absentees)}")
print("Absent Students:", absentees)
