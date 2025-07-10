#12. Python Calculator
# • Define functions for +, –, ×, ÷
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

# • Pass them as arguments to a calculator() function
def calculator(a, b, operation):
    return operation(a, b)

# • Choose operation dynamically
print("Select operation: +, -, *, /")
op = input("Enter operation: ")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if op == '+':
    result = calculator(x, y, add)
elif op == '-':
    result = calculator(x, y, sub)
elif op == '*':
    result = calculator(x, y, mul)
elif op == '/':
    result = calculator(x, y, div)
else:
    result = "Invalid operation"

print("Result:", result)
