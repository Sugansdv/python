## 8. Simple Calculator

print("========================================")
print("            Simple Calculator           ")
print("========================================")

# 1. Prompt the user for two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose operation (add, subtract, multiply, divide): ")

# 2. Perform the calculation based on the chosen operation
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation"

# 3. Print the result
print(f"\n Result: {result}")

# 4. Show types of all inputs and the result
print("\n Data Types:")
print(f"Type of num1     : {type(num1)}")
print(f"Type of num2     : {type(num2)}")
print(f"Type of operation: {type(operation)}")
print(f"Type of result   : {type(result)}")
