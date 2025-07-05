# Topper Finder in Class

# Use dictionary: student → marks
students = {
    "Dharun": 85,
    "Vishwa": 92,
    "Sugan": 78,
    "Santoz": 95,
    "Manoj": 88
}

# Use loop to find max
topper_name = ""
topper_marks = 0

for name, marks in students.items():
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

# Print topper name and mark
print("\n========= Class Topper =========")
print(f"Topper Name : {topper_name}")
print(f"Topper Marks: {topper_marks}")
print("================================")
