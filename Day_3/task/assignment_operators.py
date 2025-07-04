# 🖊️ Assignment Operators Tasks (21–26)

# Task 21: Initialize a variable with 10 and use +=, -=, *=, /=, //=, %= to update its value.
print(" Task 21: Demonstrate All Assignment Operators on a Single Variable")
x = 10
print(f"Initial value: x = {x}")
x += 5
print(f"After x += 5  →  x = {x}")
x -= 3
print(f"After x -= 3  →  x = {x}")
x *= 2
print(f"After x *= 2  →  x = {x}")
x /= 4
print(f"After x /= 4  →  x = {x}")
x //= 2
print(f"After x //= 2  →  x = {x}")
x %= 3
print(f"After x %= 3  →  x = {x}")

# Task 22: Take a number and increment it by 5 using +=.
print("\n Task 22: Increment a Number by 5 Using +=")
num = int(input("Enter a number: "))
num += 5
print(f"Updated number after += 5: {num}")

# Task 23: Calculate area of a square and double it using *=.
print("\n Task 23: Area of Square Doubled Using *=")
side = float(input("Enter side of square: "))
area = side * side
print(f"Original area: {area}")
area *= 2
print(f"Doubled area: {area}")

# Task 24: Take a salary amount and apply tax deduction using -=.
print("\n Task 24: Apply Tax Deduction on Salary Using -=")
salary = float(input("Enter your salary: ₹"))
tax = float(input("Enter tax amount to deduct: ₹"))
salary -= tax
print(f"Salary after tax deduction: ₹{salary}")

# Task 25: Modify a variable step-by-step using every assignment operator.
print("\n Task 25: Modify a Variable Step-by-Step with Assignment Operators")
v = 20
print(f"Start: v = {v}")
v += 10
print(f"After += 10  →  v = {v}")
v -= 5
print(f"After -= 5  →  v = {v}")
v *= 2
print(f"After *= 2  →  v = {v}")
v /= 5
print(f"After /= 5  →  v = {v}")
v //= 2
print(f"After //= 2  →  v = {v}")
v %= 3
print(f"After %= 3  →  v = {v}")

# Task 26: Mini bank balance simulator using assignment operators
print("\n Task 26: Mini Bank Balance Simulator")
balance = float(input("Enter initial bank balance: ₹"))
deposit = float(input("Enter deposit amount: ₹"))
balance += deposit
print(f"After deposit, balance = ₹{balance}")
withdraw = float(input("Enter withdrawal amount: ₹"))
balance -= withdraw
print(f"After withdrawal, balance = ₹{balance}")
