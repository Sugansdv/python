# 8. Recursive Factorial & Fibonacci Generator

# • One function to generate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# • Another to return nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Factorial of 5:", factorial(5))
print("Fibonacci of 6:", fibonacci(6))
