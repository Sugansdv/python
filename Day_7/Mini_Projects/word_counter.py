#3. Word Frequency Counter
# Input: a paragraph from the user
paragraph = input("Enter a paragraph: ")

# Convert string to lowercase for uniformity
paragraph = paragraph.lower()

# Split paragraph into words
words = paragraph.split()

# Print total number of words using len() on .split()
print("Total number of words:", len(words))

# Count occurrences of each word using .count()
unique_words = set(words) 
print("\nWord Frequencies:")
for word in unique_words:
    print(f"{word}: {words.count(word)}")
