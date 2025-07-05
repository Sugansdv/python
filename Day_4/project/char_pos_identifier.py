# ==== MINI PROJECT 19: CHARACTER POSITION IDENTIFIER ====

print("====================")
print("Character Position Identifier")
print("====================")

# Input: name
name = input("Enter a name: ")

# Use enumerate() to print index and character
for index, char in enumerate(name):
    print(f"{index} - {char}")
