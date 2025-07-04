
print("=======================================")
print("             Basic Chat Filter App             ")
print("=======================================\n")

# Predefined list of banned words
banned_words = ["spam", "scam", "fake", "abuse", "badword"]

# Input: User message
message = input("Enter your message: ").lower()

# Check if message contains any banned word
found_banned = False
for word in banned_words:
    if word in message:
        found_banned = True
        break

# Warning or approval based on presence of banned word
if found_banned:
    print("\n Message blocked! It contains banned or inappropriate content.")
else:
    print("\n Message sent successfully.")
