# ==== MINI PROJECT 2: VOWEL COUNTER APP ====

print("====================")
print("Vowel Counter App")
print("====================")

# Input: any string
sentence = input("Enter a sentence: ")

# Use a for loop to iterate through each character
# Use if and 'in' to check for vowels
# Use .lower() to ensure case-insensitive comparison
vowels = "aeiou"
count = 0

for char in sentence:
    if char.lower() in vowels:
        count += 1

# Display total vowel count
print(f"\nTotal number of vowels: {count}")
