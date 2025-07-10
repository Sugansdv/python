#18. Character Frequency Analyzer
# Input: sentence from the user
sentence = input("Enter a sentence: ")  

# Convert the sentence to lowercase to make counting case-insensitive
sentence = sentence.lower()

# Define vowels to check frequency
vowels = "aeiou"

# Loop through each vowel and count its occurrences using .count()
print("\nVowel Frequency:")
for vowel in vowels:
    count = sentence.count(vowel)
    print(f"{vowel} → {count}")

