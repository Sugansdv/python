# ==== MINI PROJECT 9: NUMBER TYPE CLASSIFIER ====

print("====================")
print("Number Type Classifier")
print("====================")

# Input: a list of 10 numbers
numbers_input = input("Enter 10 numbers separated by commas: ")
numbers = [int(n.strip()) for n in numbers_input.split(',')]

# Create separate lists for odd and even
odd_numbers = []
even_numbers = []

# Use for loop + if condition
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Display both lists
print("\nEven Numbers:", even_numbers)
print("Odd Numbers :", odd_numbers)
