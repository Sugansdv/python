
print("=======================================")
print("             Simple Calculator App             ")
print("=======================================\n")

# Input: Two numbers and operation symbol
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /, %, **): ")

# Use if-elif-else to perform operation
if operation == "+":
    result = num1 + num2
    symbol = "+"
elif operation == "-":
    result = num1 - num2
    symbol = "-"
elif operation == "*":
    result = num1 * num2
    symbol = "*"
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        symbol = "/"
    else:
        result = "Undefined (division by zero)"
        symbol = "/"
elif operation == "%":
    result = num1 % num2
    symbol = "%"
elif operation == "**":
    result = num1 ** num2
    symbol = "**"
else:
    result = "Invalid operation"
    symbol = "?"

# Formatted Output
print("\n========== Result ============")
print(f"Operation: {num1} {symbol} {num2}")
print(f"Result   : {result}")
print("================================")
