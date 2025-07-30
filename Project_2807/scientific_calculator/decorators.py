import math
from functools import wraps

def radians_to_degrees(func):
    @wraps(func)
    def wrapper(x):
        degrees = math.radians(x)
        return func(degrees)
    return wrapper
