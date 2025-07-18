from decimal import Decimal
import math

def power(a, b):
    return Decimal(a) ** Decimal(b)

def square_root(a):
    a = Decimal(a)
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return Decimal(math.sqrt(float(a)))

def logarithm(a, base=10):
    a = Decimal(a)
    if a <= 0:
        raise ValueError("Logarithm input must be positive.")
    return Decimal(math.log(float(a), float(base)))
