import time
import math
from functools import wraps

# Helper for all: Decorator template
def preserve_metadata(decorator):
    @wraps(decorator)
    def wrapper(func):
        return wraps(func)(decorator(func))
    return wrapper

# 1. Double and square result
def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

def square_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

# 2. Authenticate and Authorize
def authenticate(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated"):
            print("User not authenticated")
            return None
        return func(user, *args, **kwargs)
    return wrapper

def authorize(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            print("User not authorized")
            return None
        return func(user, *args, **kwargs)
    return wrapper

# 3. log_input and log_output
def log_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Input] {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def log_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[Output] {result}")
        return result
    return wrapper

# 4. Reverse + Uppercase a string
def reverse_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)[::-1]
    return wrapper

def uppercase_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

# 5. Format HTML: <p> and <div>
def html_p(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}</p>"
    return wrapper

def html_div(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<div>{func(*args, **kwargs)}</div>"
    return wrapper

# 6. CLI chain: log, time, format
def cli_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("[CLI] Command started")
        return func(*args, **kwargs)
    return wrapper

def cli_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[CLI] Took {time.time() - start:.3f}s")
        return result
    return wrapper

def cli_format(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f">>> {func(*args, **kwargs)}"
    return wrapper

# 7. Math chain: log result, check even
def log_math(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[Math Result]: {result}")
        return result
    return wrapper

def is_even(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Even" if result % 2 == 0 else "Odd")
        return result
    return wrapper

# 8. Validate input + transform result
def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x < 0:
            print("Negative input not allowed")
            return None
        return func(x)
    return wrapper

def double_output(func):
    @wraps(func)
    def wrapper(x):
        return func(x) * 2
    return wrapper

# 9. Pipeline simulation
def stage1(func):
    @wraps(func)
    def wrapper(data):
        result = f"{data}-Stage1"
        return func(result)
    return wrapper

def stage2(func):
    @wraps(func)
    def wrapper(data):
        result = f"{data}-Stage2"
        return func(result)
    return wrapper

def stage3(func):
    @wraps(func)
    def wrapper(data):
        result = f"{data}-Stage3"
        return func(result)
    return wrapper

# 10. Use functools.wraps everywhere (already done above)

# =============================
# Example Usages for Each Task
# =============================

@double_result
@square_result
def task1():
    return 3

@authenticate
@authorize
def task2(user):
    print(f"Access granted to {user['name']}")

@log_input
@log_output
def task3(x, y):
    return x * y

@reverse_string
@uppercase_string
def task4():
    return "chained decorators"

@html_p
@html_div
def task5():
    return "Formatted Content"

@cli_log
@cli_time
@cli_format
def task6():
    time.sleep(0.5)
    return "CLI Task Complete"

@is_even
@log_math
def task7():
    return 42

@double_output
@validate_positive
def task8(x):
    return x + 5

@stage1
@stage2
@stage3
def task9(data):
    return f"Final: {data}"

# =============================
# Run All Tasks
# =============================
if __name__ == "__main__":
    print("1:", task1())  # (3^2) * 2 = 18
    print("2:")
    task2({'name': 'Alice', 'authenticated': True, 'role': 'admin'})
    task2({'name': 'Bob', 'authenticated': False, 'role': 'admin'})
    print("3:", task3(2, 5))
    print("4:", task4())
    print("5:", task5())
    print("6:", task6())
    print("7:", task7())
    print("8:", task8(10))
    print("9:", task9("Data"))
