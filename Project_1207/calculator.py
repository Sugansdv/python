# 7. Text-Based Calculator
# Concepts: functions, strings, lists.
# • Ask user to input operation (add, subtract, etc.).
# • Use functions for each operation.
# • Store past results in a list.
# • Loop until user exits.

results = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

while True:
    print("\nOperations: add, subtract, multiply, divide, history, exit")
    op = input("Enter operation: ").strip().lower()

    if op == "exit":
        break
    elif op == "history":
        print("\n--- Calculation History ---")
        for res in results:
            print(res)
        continue
    elif op in ["add", "subtract", "multiply", "divide"]:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
            a, b = float(num1), float(num2)
            if op == "add":
                result = add(a, b)
            elif op == "subtract":
                result = subtract(a, b)
            elif op == "multiply":
                result = multiply(a, b)
            elif op == "divide":
                result = divide(a, b)
            print(f"Result: {result}")
            results.append(f"{op}({a}, {b}) = {result}")
        else:
            print("Invalid input. Please enter numbers.")
    else:
        print("Unknown operation.")
