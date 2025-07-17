# 20. Class Schedule Collision Detector
# Goal: Detect conflicting class schedules.
# Requirements:
# - Store class slots as sets.
# - Use intersection() to find conflicts.
# - Suggest available slots using difference().
# Concepts Covered: intersection(), difference(), add().

math_slots = {"Mon 9AM", "Wed 11AM", "Fri 2PM"}
science_slots = {"Mon 9AM", "Tue 10AM", "Thu 1PM"}
available_slots = {"Mon 9AM", "Tue 10AM", "Wed 11AM", "Thu 1PM", "Fri 2PM", "Fri 4PM"}

conflicts = math_slots.intersection(science_slots)
suggested_slots = available_slots.difference(math_slots.union(science_slots))

print("Conflicting slots:", conflicts)
print("Suggested available slots:", suggested_slots)
