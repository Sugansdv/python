#8. Sentence Analyzer
# Input: sentence from the user
sentence = input("Enter a sentence: ")

# Print the first character using indexing
print("First character:", sentence[0])

# Print the last character using indexing
print("Last character:", sentence[-1])

# Find the position of the first space using .find()
space_pos = sentence.find(" ")
print("First space position:", space_pos)

# Count total vowels using .count() in a loop
vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in sentence if ch in vowels)

# Count total spaces using .count(" ")
space_count = sentence.count(" ")

# Print total vowels and spaces
print("Total vowels:", vowel_count)
print("Total spaces:", space_count)

