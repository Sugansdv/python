# 18. College Course Manager
# Goal: Manage courses offered in a semester.
# Requirements:
# • Each course: (course_id, name, (credits, faculty))
# • Sort courses by credits.
# • Use count() to see how many courses a faculty handles.
# • Display using unpacked formatting.

# List of courses
courses = [
    ("CS101", "Data Structures", (4, "Dr. Rao")),
    ("MA201", "Calculus", (3, "Dr. Sharma")),
    ("PH110", "Physics", (4, "Dr. Rao")),
    ("EN101", "English", (2, "Dr. Verma")),
    ("CS102", "Algorithms", (5, "Dr. Rao"))
]

# Display courses using unpacking
print(" Semester Course List:\n")
for course_id, name, (credits, faculty) in courses:
    print(f"{course_id} - {name} ({credits} credits) | Faculty: {faculty}")

# Sort courses by credits
sorted_courses = sorted(courses, key=lambda c: c[2][0], reverse=True)

print("\n Courses Sorted by Credits:\n")
for course_id, name, (credits, faculty) in sorted_courses:
    print(f"{course_id} - {name} ({credits} credits)")

# Count how many courses Dr. Rao handles
faculty_name = "Dr. Rao"
handled = sum(1 for _, _, (_, f) in courses if f == faculty_name)
print(f"\n {faculty_name} handles {handled} course(s).")
