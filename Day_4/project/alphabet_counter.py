# ==== MINI PROJECT 14: ALPHABET COUNTER ====

print("====================")
print("Alphabet Counter")
print("====================")

# Input: string
text = input("Enter any text: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
special_chars = 0

# Use for loop + if conditions + in + .isalpha() or .isdigit()
for char in text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1

# Display result
print("\nCharacter Count Report:")
print(f"Vowels          : {vowels}")
print(f"Consonants      : {consonants}")
print(f"Digits          : {digits}")
print(f"Special Chars   : {special_chars}")
