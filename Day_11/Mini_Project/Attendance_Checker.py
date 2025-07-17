# 8. Student Attendance Checker
# Goal: Mark students present using sets.
# Requirements:
# - Store enrolled and present students in sets.
# - Compare with difference() to find absentees.
# - Add latecomers using add() or update().
# Concepts Covered: Membership, add(), update(), set diff.

enrolled = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
present = {"Alice", "Charlie", "Eve"}

absentees = enrolled.difference(present)
present.add("Bob")
present.update(["Diana"])

print("Absentees before latecomers:", absentees)
print("Final present list:", present)
