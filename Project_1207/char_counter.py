# 9. Character Frequency Counter
# Concepts: strings, lists, functions.
# • Input a sentence.
# • Count frequency of each character.
# • Return output in dictionary or formatted string.
# • Use functions to handle logic.

def count_characters(text):
    freq = {}
    for char in text:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return freq

sentence = input("Enter a sentence: ")
result = count_characters(sentence)

print("\n--- Character Frequencies ---")
for char, count in result.items():
    print(f"'{char}': {count}")
