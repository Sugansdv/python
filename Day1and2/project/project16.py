## 16. Odd/Even Number Identifier

print("========================================")
print("         Odd/Even Number Checker        ")
print("========================================")

# 1. Ask the user for a number
num_input = input("Enter a number: ")

# 2. Print the type before conversion
print(f"Type before conversion: {type(num_input)}")

# 3. Convert the input to an integer
number = int(num_input)

# 4. Print the type after conversion
print(f"Type after conversion: {type(number)}")

# 5. Check and print if it's odd or even
if number % 2 == 0:
    print(f"\n {number} is an Even number.")
else:
    print(f"\n {number} is an Odd number.")
