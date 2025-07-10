#11. Feedback Cleaner Tool
# Input feedback from the user
feedback = input("Enter your feedback: ") 

# Remove extra spaces from both ends using .strip()
cleaned = feedback.strip()

# Remove all exclamation marks using .replace()
cleaned = cleaned.replace("!", "")

# Count number of words using .split() and len()
word_count = len(cleaned.split())

# Count number of characters (excluding spaces) using len() and .replace(" ", "")
char_count = len(cleaned.replace(" ", ""))

# Print cleaned feedback, word count, and character count
print("\nCleaned Feedback:", cleaned)
print("Total Words:", word_count)
print("Total Characters (no spaces):", char_count)

