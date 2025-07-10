#10. String Transformer
# Input a sentence from the user
sentence = input("Enter a sentence: ")  # Example: Python is Powerful

# Convert entire sentence to uppercase
upper_case = sentence.upper()

# Convert entire sentence to lowercase
lower_case = sentence.lower()

# Convert sentence to title case (first letter capitalized for each word)
title_case = sentence.title()

# Replace all spaces with underscores using .replace()
underscored = sentence.replace(" ", "_")

print("\nAll Uppercase:", upper_case)
print("All Lowercase:", lower_case)
print("Title Case:", title_case)
print("With Underscores:", underscored)

