# 17. Word Counter Tool
# Concepts: string, list, functions.
# • Input paragraph from user.
# • Count words using split().
# • Count specific word frequency.

def count_words(text):
    words = text.split()
    return len(words)

def word_frequency(text, word):
    words = text.lower().split()
    return words.count(word.lower())

paragraph = input("Enter a paragraph:\n")
total_words = count_words(paragraph)
print(f"\nTotal words: {total_words}")

target = input("Enter a word to count its frequency: ")
freq = word_frequency(paragraph, target)
print(f"'{target}' appears {freq} time(s)")
