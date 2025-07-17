# 3. Course Enrollment Analyzer
# Goal: Compare students enrolled in two different courses.
# Requirements:
# - Store Python and Java student names in sets.
# - Find students enrolled in both (intersection).
# - Find exclusive Python students (difference).
# - Combine both courses (union).
# - Find students in only one course (symmetric_difference).
# Concepts Covered: union(), intersection(), difference(), symmetric_difference().

python_students = {"Alice", "Bob", "Charlie", "Diana"}
java_students = {"Charlie", "Eve", "Bob", "Frank"}

both_courses = python_students.intersection(java_students)
only_python = python_students.difference(java_students)
all_students = python_students.union(java_students)
only_one_course = python_students.symmetric_difference(java_students)

print("Students in both courses:", both_courses)
print("Exclusive Python students:", only_python)
print("All students in either course:", all_students)
print("Students in only one course:", only_one_course)
