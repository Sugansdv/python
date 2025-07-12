# 2. Student Score Tracker
# Description: Maintain student names and marks using lists and nested lists.

# Use a nested list format: [['Ram', 85], ['Sam', 78]]
students = [['Ram', 85], ['Sam', 78], ['Dharun', 92], ['Vishwa', 67]]

# Access and update specific student’s marks
for student in students:
    if student[0] == 'Sam':
        student[1] = 80
print("Updated Sam's marks to 80.")

# Add a new student
students.append(['Vikram', 88])
print("\nAdded new student: Vikram")

# Remove a student
students.remove(['Vishwa', 67])
print("Removed student: Priya")

# Display all students and their marks
print("\nAll Students:")
for name, score in students:
    print(f"{name} - {score}")

# Sort or analyze scores (highest/lowest)
students.sort(key=lambda x: x[1], reverse=True)
print("\nStudents sorted by score (high to low):")
for name, score in students:
    print(f"{name} - {score}")

# Find highest and lowest scorer
highest = max(students, key=lambda x: x[1])
lowest = min(students, key=lambda x: x[1])
print(f"\nHighest scorer: {highest[0]} with {highest[1]} marks")
print(f"Lowest scorer: {lowest[0]} with {lowest[1]} marks")
