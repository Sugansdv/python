import time
import functools
import logging

# --- Setup logger ---
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("MathLogger")

# --- Decorator: Validate inputs ---
def validate_numeric_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("All arguments must be numeric (int or float)")
        return func(*args, **kwargs)
    return wrapper

# --- Decorator: Log output ---
def log_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"[LOG] {func.__name__}({', '.join(map(str, args))}) = {result}")
        return result
    return wrapper

# --- Decorator: Time execution ---
def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"[TIME] {func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

# --- Decorated Math Functions ---
@timeit
@log_output
@validate_numeric_input
def add(a, b):
    return a + b

@timeit
@log_output
@validate_numeric_input
def multiply(a, b):
    return a * b

@timeit
@log_output
@validate_numeric_input
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(add(5, 3))
    print(multiply(4, 6))
    print(divide(10, 2))

    # Uncomment to test validation
    # print(add(5, "two"))
    # print(divide(5, 0))
