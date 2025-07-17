# 15. Book Club Member Organizer
# Goal: Manage participants across book clubs.
# Requirements:
# - Use sets for each club.
# - Use intersection() to find common members.
# - Use symmetric_difference() to find club-exclusive readers.
# Concepts Covered: All set operations.

fiction_club = {"Alice", "Bob", "Charlie", "Diana"}
history_club = {"Charlie", "Diana", "Edward", "Fiona"}

common_members = fiction_club.intersection(history_club)
exclusive_members = fiction_club.symmetric_difference(history_club)

print("Common members in both clubs:", common_members)
print("Members in only one club:", exclusive_members)
