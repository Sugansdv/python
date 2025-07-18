# test_runner.py

# Task 1: math_tools.py
import math_tools

print("\n--- Task 1: math_tools ---")
print("Add(5, 3):", math_tools.add(5, 3))
print("Subtract(5, 3):", math_tools.subtract(5, 3))
print("Multiply(5, 3):", math_tools.multiply(5, 3))
print("Divide(5, 3):", math_tools.divide(5, 3))
print("Divide(5, 0):", math_tools.divide(5, 0))  # Edge case

# Task 2: greetings.py
import greetings

print("\n--- Task 2: greetings ---")
greetings.greet_user("Alice")
greetings.greet_user("Bob")

# Task 3: temperature_converter.py
import temperature_converter

print("\n--- Task 3: temperature_converter ---")
print("0°C to °F:", temperature_converter.celsius_to_fahrenheit(0))
print("100°F to °C:", temperature_converter.fahrenheit_to_celsius(100))

# Task 4 & 5: geometry.py with PI constant
import geometry

print("\n--- Task 4 & 5: geometry ---")
print("Area of Circle (r=3):", geometry.area_circle(3))
print("Perimeter of Circle (r=3):", geometry.perimeter_circle(3))
print("Area of Square (side=4):", geometry.area_square(4))
print("Perimeter of Square (side=4):", geometry.perimeter_square(4))
print("Area of Triangle (base=4, height=5):", geometry.area_triangle(4, 5))
print("Perimeter of Triangle (3, 4, 5):", geometry.perimeter_triangle(3, 4, 5))

# Task 8: individual modules
import addition, subtraction, multiplication, division

print("\n--- Task 8: Split math modules ---")
print("Addition (10 + 2):", addition.add(10, 2))
print("Subtraction (10 - 2):", subtraction.subtract(10, 2))
print("Multiplication (10 * 2):", multiplication.multiply(10, 2))
print("Division (10 / 2):", division.divide(10, 2))
print("Division (10 / 0):", division.divide(10, 0))  # Edge case
