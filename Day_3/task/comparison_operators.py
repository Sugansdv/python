# 🧮 Comparison Operators Tasks (9–14)

# Task 9: Compare two user-input numbers using all 6 comparison operators and print results.
print(" Task 9: Compare Two Numbers Using All Comparison Operators")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"{num1} == {num2} →  {num1 == num2}")
print(f"{num1} != {num2} →  {num1 != num2}")
print(f"{num1} > {num2} →  {num1 > num2}")
print(f"{num1} < {num2} →  {num1 < num2}")
print(f"{num1} >= {num2} →  {num1 >= num2}")
print(f"{num1} <= {num2} →  {num1 <= num2}")

# Task 10: Write a program to check if a person is older than 18.
print("\n Task 10: Check If Person is Older Than 18")
age = int(input("Enter your age: "))
if age > 18:
    print("You are older than 18 ")
else:
    print("You are 18 or younger ")

# Task 11: Take two strings and check if they are equal or not using ==, !=.
print("\n Task 11: String Equality Check")
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print(f"Strings are equal: {str1 == str2}")
print(f"Strings are not equal: {str1 != str2}")

# Task 12: Ask for two exam scores and compare which one is higher using >, <.
print("\n Task 12: Compare Two Exam Scores")
score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
if score1 > score2:
    print("Score 1 is higher ")
elif score1 < score2:
    print("Score 2 is higher ")
else:
    print("Both scores are equal ")

# Task 13: Use >= and <= to check if the number lies in a particular range.
print("\n Task 13: Check if Number Lies Within a Range (10 to 100)")
num = float(input("Enter a number: "))
if 10 <= num <= 100:
    print("Number lies within the range 10–100 ")
else:
    print("Number is outside the range ")

# Task 14: Create a simple program to check if a user entered score is a passing mark (above 50).
print("\n Task 14: Check If Score is a Passing Mark (> 50)")
mark = float(input("Enter your score: "))
if mark > 50:
    print("Congratulations! You passed ")
else:
    print("You did not pass. Better luck next time ")
