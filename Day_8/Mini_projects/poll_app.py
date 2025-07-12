# 8. Simple Poll App
# Description: Take responses to a question and analyze results.

# Store answers in a list (some valid, some invalid for testing)
responses = ["Yes", "No", "yes", "No", "Maybe", "YES", "no", "Yess", "No", "yes"]

# Normalize inputs (convert all to lowercase)
normalized_responses = [resp.lower() for resp in responses]

# Remove incorrect inputs (only keep 'yes' or 'no')
valid_responses = []
for resp in normalized_responses:
    if resp in ["yes", "no"]:
        valid_responses.append(resp)

# Count how many voted "yes" or "no"
yes_count = valid_responses.count("yes")
no_count = valid_responses.count("no")

# Display results
print(" Poll Results:")
print(f"Total responses collected: {len(responses)}")
print(f"Valid responses: {len(valid_responses)}")
print(f"Yes: {yes_count}")
print(f"No: {no_count}")
print(f"Ignored invalid responses: {len(responses) - len(valid_responses)}")
