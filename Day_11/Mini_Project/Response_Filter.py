# 4. Survey Response Filter
# Goal: Clean up survey responses for analysis.
# Requirements:
# - Store each response ID in a set.
# - Add new responses with update().
# - Remove invalid responses with remove() and discard().
# - Track removed responses separately.
# - Use pop() to test random removal.
# Concepts Covered: update(), remove(), discard(), pop().

responses = {"R001", "R002", "R003", "R004"}
responses.update({"R005", "R006", "R002", "R007"})

removed_responses = set()

try:
    responses.remove("R003")
    removed_responses.add("R003")
except KeyError:
    pass

responses.discard("R010")
removed_responses.add("R010")

random_removed = responses.pop()
removed_responses.add(random_removed)

print("Cleaned responses:", responses)
print("Removed responses:", removed_responses)
