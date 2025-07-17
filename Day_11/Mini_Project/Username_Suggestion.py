# 12. Username Suggestion System
# Goal: Suggest new usernames without duplicates.
# Requirements:
# - Store taken usernames in a set.
# - Check new suggestions with in.
# - Keep only valid and unique suggestions.
# Concepts Covered: Membership, add(), discard().

taken_usernames = {"john_doe", "alice123", "coolguy"}
suggestions = ["john_doe", "alice_w", "coolguy", "new_user"]

valid_suggestions = []
for username in suggestions:
    if username not in taken_usernames:
        taken_usernames.add(username)
        valid_suggestions.append(username)

print("Valid suggestions:", valid_suggestions)
print("Updated taken usernames:", taken_usernames)
