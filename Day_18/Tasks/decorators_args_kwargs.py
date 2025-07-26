from functools import wraps

# 1. Log all arguments
def log_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Positional: {args}, Keyword: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# 2. Sum all arguments
def sum_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        total = sum(arg for arg in args if isinstance(arg, (int, float)))
        print(f"[SUM] Total of numeric args: {total}")
        return func(*args, **kwargs)
    return wrapper

# 3. Validate argument types using isinstance
def validate_types(*expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Argument {arg} is not of type {expected.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 4. Ensure string argument is not empty
def non_empty_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str) and arg.strip() == "":
                raise ValueError("Empty string argument not allowed")
        return func(*args, **kwargs)
    return wrapper

# 5. Enforce at least one keyword argument
def require_kwarg(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs:
            raise ValueError("At least one keyword argument required")
        return func(*args, **kwargs)
    return wrapper

# 6. Allow only int arguments
def only_ints(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError("Only integer arguments allowed")
        return func(*args, **kwargs)
    return wrapper

# 7. Reverse list argument
def reverse_list_arg(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = tuple(arg[::-1] if isinstance(arg, list) else arg for arg in args)
        return func(*new_args, **kwargs)
    return wrapper

# 8. Convert all string args to lowercase
def lowercase_strings(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = tuple(arg.lower() if isinstance(arg, str) else arg for arg in args)
        new_kwargs = {k: v.lower() if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper

# 9. Round float return values to 2 decimals
def round_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, float):
            return round(result, 2)
        return result
    return wrapper

# 10. Block execution if block=True
def block_if_flagged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get("block"):
            print("[BLOCKED] Function execution skipped.")
            return None
        return func(*args, **kwargs)
    return wrapper

# ===============================
# Example Usages for Each Task
# ===============================

@log_args
def task1(a, b, c=0):
    return a + b + c

@sum_args
def task2(a, b, c):
    return a + b + c

@validate_types(int, str)
def task3(x, y):
    return f"{x} and {y}"

@non_empty_string
def task4(msg):
    return f"Message: {msg}"

@require_kwarg
def task5(x, **kwargs):
    return f"x={x}, kwargs={kwargs}"

@only_ints
def task6(a, b, c):
    return a + b + c

@reverse_list_arg
def task7(my_list):
    return my_list

@lowercase_strings
def task8(name, city=""):
    return f"{name} from {city}"

@round_result
def task9():
    return 3.14159

@block_if_flagged
def task10(x, block=False):
    return f"Executed with x={x}"

# ===============================
# Run Tasks
# ===============================
if __name__ == "__main__":
    print("1:", task1(1, 2, c=3))
    print("2:", task2(4, 5, 6))
    print("3:", task3(10, "decorator"))
    print("4:", task4("Hello!"))
    print("5:", task5(99, mode="test"))
    print("6:", task6(1, 2, 3))
    print("7:", task7([10, 20, 30]))
    print("8:", task8("JOHN", city="LONDON"))
    print("9:", task9())
    print("10a:", task10(42))
    print("10b:", task10(42, block=True))
