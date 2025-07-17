# 18. Vocabulary Builder from Articles
# Goal: Extract unique words from news articles.
# Requirements:
# - Read words from multiple files.
# - Use set comprehension to build a unique vocabulary set.
# - Print words not in the user’s known word list.
# Concepts Covered: Set comp, difference(), file-to-set.

# Simulating file reading with string content
article1 = "Python is a powerful programming language"
article2 = "Language learning requires practice and consistency"

words1 = {word.lower() for word in article1.split()}
words2 = {word.lower() for word in article2.split()}

vocabulary = words1.union(words2)
known_words = {"python", "language", "learning"}

new_words = vocabulary.difference(known_words)

print("Full vocabulary set:", vocabulary)
print("New words to learn:", new_words)
