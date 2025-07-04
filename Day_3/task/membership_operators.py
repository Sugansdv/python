# 📜 Membership Operators Tasks (31–35)

# Task 31: Check if a letter is present in a string using in.
print(" Task 31: Check if a Letter is in a String")
text = input("Enter a string: ")
letter = input("Enter a letter to search: ")
if letter in text:
    print(f"'{letter}' is present in the string ")
else:
    print(f"'{letter}' is not present in the string ")

# Task 32: Ask user for a fruit name and check if it is in your predefined fruit list.
print("\n Task 32: Check if Entered Fruit is in the List")
fruits = ["apple", "banana", "mango", "orange"]
fruit_input = input("Enter a fruit name: ").lower()
if fruit_input in fruits:
    print(f"{fruit_input.title()} is available ")
else:
    print(f"{fruit_input.title()} is not in the list ")

# Task 33: Use not in to check if a number is not in a list.
print("\n Task 33: Check if Number is Not in List")
numbers = [1, 3, 5, 7, 9]
num = int(input("Enter a number: "))
if num not in numbers:
    print(f"{num} is not in the list ")
else:
    print(f"{num} is in the list ")

# Task 34: Search for a word in a sentence using in and display if it’s found.
print("\n Task 34: Search for a Word in a Sentence")
sentence = input("Enter a sentence: ").lower()
search_word = input("Enter word to search: ").lower()
if search_word in sentence:
    print(f"The word '{search_word}' is found in the sentence ")
else:
    print(f"The word '{search_word}' is not found ")

# Task 35: Check if a key exists in a dictionary using in.
print("\n Task 35: Check if Key Exists in Dictionary")
student = {
    "name": "Dharun",
    "age": 20,
    "grade": "A"
}
key_input = input("Enter key to search (e.g., name, age): ").lower()
if key_input in student:
    print(f"'{key_input}' exists in the student dictionary ")
else:
    print(f"'{key_input}' does not exist ")
