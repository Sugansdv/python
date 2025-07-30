import math
from decorators import radians_to_degrees

@radians_to_degrees
def sin(x):
    return math.sin(x)

@radians_to_degrees
def cos(x):
    return math.cos(x)

@radians_to_degrees
def tan(x):
    return math.tan(x)

def log(x, base=10):
    return math.log(x, base)

def sqrt(x):
    return math.sqrt(x)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
