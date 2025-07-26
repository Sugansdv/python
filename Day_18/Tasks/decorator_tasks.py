import time
from functools import wraps
from datetime import datetime

# 1. Basic "Function started" decorator
def print_start(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        return func(*args, **kwargs)
    return wrapper

# 2. Print function name decorator
def print_function_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 3. Count function calls
def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Call count: {wrapper.call_count}")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

# 4. Return square of return value
def square_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

# 5. Convert return to uppercase
def to_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs)).upper()
    return wrapper

# 6. Log function args and return
def log_args_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return: {result}")
        return result
    return wrapper

# 7. Logging before and after function
def log_before_after(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

# 8. Add exception handling
def catch_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception caught: {e}")
            return None
    return wrapper

# 9. Execution time
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

# 10. Log datetime before run
def log_datetime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Current datetime: {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

# Example usages

@print_start
def task1():
    print("Task 1 executed")

@print_function_name
def task2():
    print("Task 2 executed")

@count_calls
def task3():
    print("Task 3 executed")

@square_return
def task4():
    return 5

@to_uppercase
def task5():
    return "hello decorators"

@log_args_return
def task6(x, y):
    return x + y

@log_before_after
def task7():
    print("Doing task 7")

@catch_exception
def task8():
    return 10 / 0  # Will raise ZeroDivisionError

@measure_time
def task9():
    time.sleep(1)
    print("Finished task 9")

@log_datetime
def task10():
    print("Running task 10")

# Run all tasks
if __name__ == "__main__":
    task1()
    task2()
    task3(); task3()
    print("Task 4 Output:", task4())
    print("Task 5 Output:", task5())
    task6(3, 7)
    task7()
    task8()
    task9()
    task10()
