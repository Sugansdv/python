## Basic For Loop Tasks (1–10)
# Task 1: Print all elements in the list ["Pen", "Pencil", "Eraser"]
items = ["Pen", "Pencil", "Eraser"]
for item in items:
    print(item)

print('-' * 30)

# Task 2: Print each character in the string "Vetri"
for char in "Vetri":
    print(char)

print('-' * 30)

# Task 3: Use range() to print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print('-' * 30)

# Task 4: Print all odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i)

print('-' * 30)

# Task 5: Create a list of 5 colors and print them
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
for color in colors:
    print(color)

print('-' * 30)

# Task 6: Use range() to print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

print('-' * 30)

# Task 7: Ask user to enter a number n, and print numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

print('-' * 30)

# Task 8: Create a list of fruits and print “I like <fruit>”
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
for fruit in fruits:
    print(f"I like {fruit}")

print('-' * 30)

# Task 9: Print the multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

print('-' * 30)

# Task 10: Calculate the sum of numbers from 1 to 50
total = 0
for i in range(1, 51):
    total += i
print("Sum of numbers from 1 to 50 is:", total)

## For Loop with Strings (11–15)
# Task 11: Print all vowels in "Technology"
word = "Technology"
vowels = "aeiouAEIOU"
for char in word:
    if char in vowels:
        print(char)

print('-' * 30)

# Task 12: Count and display number of vowels in a given string
text = input("Enter a string : ")
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

print('-' * 30)

# Task 13: Count number of lowercase letters in "Python Loop Practice"
text = "Python Loop Practice"
lower_count = 0
for char in text:
    if char.islower():
        lower_count += 1
print("Number of lowercase letters:", lower_count)

print('-' * 30)

# Task 14: Print each word in the string "Learn Python Fast"
sentence = "Learn Python Fast"
words = sentence.split()
for word in words:
    print(word)

print('-' * 30)

# Task 15: Reverse a string using a for loop (without slicing)
original = "Programming"
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)

## Range() with For Loop (16–20)

# Task 16: Print all numbers between 1 and 50 that are divisible by 5
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

print('-' * 30)

# Task 17: Print even numbers between 2 and 20 using range(start, stop, step)
for i in range(2, 21, 2):
    print(i)

print('-' * 30)

# Task 18: Ask for a starting and ending number from the user and print the range
start = int(input("Enter starting number : "))
end = int(input("Enter ending number: "))
for i in range(start, end + 1):
    print(i)

print('-' * 30)

# Task 19: Print powers of 2 (2, 4, 8, 16, ...) up to 1024
value = 2
while value <= 1024:
    print(value)
    value *= 2

print('-' * 30)

# Task 20: Print the square of each number from 1 to 10
for i in range(1, 11):
    print(f"{i}^2 = {i**2}")
