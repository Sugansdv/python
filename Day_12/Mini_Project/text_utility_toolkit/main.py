from textutils import *
from textutils.utils import print_header

sample_text = "Hello, World! Welcome to the Text Utility Toolkit.\nLet's write clean and reusable code."

print_header("Sanitized Text")
print(remove_punctuation(sample_text))
print(to_lowercase(sample_text))
print(trim_whitespace(sample_text))

print_header("Counting Utilities")
print("Words:", count_words(sample_text))
print("Characters:", count_chars(sample_text))
print("Lines:", count_lines(sample_text))

print_header("Analysis")
print("Word Frequency:", word_frequency(sample_text))
print("Is Palindrome? ", is_palindrome("Madam"))
print("Is Anagram? ", is_anagram("Listen", "Silent"))
