# 🧮 Arithmetic Operators Tasks (1–8)

# Task 1: Take two numbers as input and print their addition, subtraction, multiplication, and division.
print(" Task 1: Basic Arithmetic Operations (+, -, *, /)")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

# Task 2: Perform floor division and modulus of two numbers and display with f-string.
print("\n Task 2: Floor Division and Modulus (//, %)")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")

# Task 3: Use exponentiation ** to calculate power of a number.
print("\n Task 3: Exponentiation (**)")
base = float(input("Enter base number: "))
power = float(input("Enter power: "))
print(f"{base} raised to the power of {power} = {base ** power}")

# Task 4: Create a calculator that takes 2 inputs and prints all arithmetic results (+, -, *, /, //, %, **).
print("\n Task 4: Full Arithmetic Calculator (+, -, *, /, //, %, **)")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Floor Division: {x // y}")
print(f"Modulus: {x % y}")
print(f"Exponentiation: {x ** y}")

# Task 5: Create a shopping app that adds the prices of 3 items.
print("\n Task 5: Shopping App – Add Prices of 3 Items")
item1 = float(input("Enter price of item 1: ₹"))
item2 = float(input("Enter price of item 2: ₹"))
item3 = float(input("Enter price of item 3: ₹"))
total_price = item1 + item2 + item3
print(f"Total Price = ₹{total_price}")

# Task 6: Ask user for marks in 5 subjects and calculate average using arithmetic operators.
print("\n Task 6: Calculate Average of Marks in 5 Subjects")
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))
m5 = float(input("Enter marks for Subject 5: "))
average = (m1 + m2 + m3 + m4 + m5) / 5
print(f"Average Marks = {average}")

# Task 7: Convert Celsius to Fahrenheit using arithmetic formula.
print("\n Task 7: Convert Celsius to Fahrenheit")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Task 8: Use print(f"") to show result of each arithmetic operation with two variables.
print("\n Task 8: Display Arithmetic Results Using f-Strings")
a = 12
b = 5
print(f"Given a = {a}, b = {b}")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
