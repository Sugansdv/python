# ==== MINI PROJECT 7: VOWEL REMOVER TOOL ====

print("====================")
print("Vowel Remover Tool")
print("====================")

# Input: sentence
sentence = input("Enter a sentence: ")

# Use a new string to collect non-vowel characters
filtered = ""
vowels = "aeiouAEIOU"

# Use for loop with continue to skip vowels
for char in sentence:
    if char in vowels:
        continue
    filtered += char

# Display the filtered sentence
print("\nSentence without vowels:")
print(filtered)
