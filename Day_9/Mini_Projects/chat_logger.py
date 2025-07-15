# 19. Chat Conversation Logger
# Goal: Store chat messages for a user.
# Requirements:
# • Each message: (timestamp, (sender, message))
# • Use slicing to get recent messages.
# • Tuple unpacking to format display.
# • Prevent edit using immutability.

# List of chat messages
chat_log = [
    ("2025-07-15 10:00", ("Alice", "Hi! How are you?")),
    ("2025-07-15 10:01", ("Bob", "I'm good, thanks!")),
    ("2025-07-15 10:02", ("Alice", "Are we still on for lunch?")),
    ("2025-07-15 10:03", ("Bob", "Absolutely, 1 PM works?")),
    ("2025-07-15 10:04", ("Alice", "Perfect. See you then!"))
]

# Display recent messages using slicing and unpacking
print(" Recent Chat Messages:\n")
for timestamp, (sender, message) in chat_log[-3:]:
    print(f"[{timestamp}] {sender}: {message}")
