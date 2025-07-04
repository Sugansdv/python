
print("=======================================")
print("           Odd or Even Number Detector          ")
print("=======================================\n")

# Input: Number
number = int(input("Enter a number: "))

# Use modulus and if-else to check even or odd
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

# Formatted output
print("\n========== Result ==========")
print(f"The number {number} is {result}.")
print("================================")