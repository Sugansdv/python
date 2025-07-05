# Feedback Analyzer

# Input: list of messages (strings)
feedback_messages = [
    "The service was really good!",
    "I had to wait too long.",
    "Good food and clean tables.",
    "It was okay, nothing special.",
    "Very good experience overall."
]

# Use for loop to classify:
# If message contains “good” → Positive, Else → Neutral
print("\n========= Feedback Analysis =========")
for msg in feedback_messages:
    if "good" in msg.lower():
        sentiment = "Positive"
    else:
        sentiment = "Neutral"
    print(f"Message: \"{msg}\" → {sentiment}")
print("=====================================")
