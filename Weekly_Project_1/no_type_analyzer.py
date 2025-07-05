# Number Type Analyzer

# Input a list of numbers
input_str = input("Enter a list of numbers (comma-separated): ")
numbers = [int(num.strip()) for num in input_str.split(",")]

# Use for loop + if to print:
# Even/Odd
# Positive/Negative
print("\n====== Number Type Analysis ======")
for num in numbers:
    # Check even or odd
    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"
    
    # Check positive or negative
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    print(f"{num} → {parity}, {sign}")
print("==================================")
