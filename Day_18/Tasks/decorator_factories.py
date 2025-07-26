import time
from functools import wraps

# 1. Repeat output n times
def repeat_output(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = [func(*args, **kwargs) for _ in range(n)]
            return results
        return wrapper
    return decorator

# 2. Log to a custom file
def log_to_file(filepath):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filepath, 'a') as f:
                f.write(f"{func.__name__} called with {args}, {kwargs} -> {result}\n")
            return result
        return wrapper
    return decorator

# 3. Limit function calls
def limit_calls(max_calls):
    def decorator(func):
        count = {'calls': 0}
        @wraps(func)
        def wrapper(*args, **kwargs):
            if count['calls'] >= max_calls:
                print(f"Function call limit of {max_calls} exceeded.")
                return None
            count['calls'] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 4. Role-based access
def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get('role') != required_role:
                print(f"Access denied: requires role '{required_role}'")
                return None
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

# 5. Minimum argument length
def min_arg_length(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if any(len(str(arg)) < n for arg in args):
                print(f"All arguments must be at least {n} characters long.")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 6. Custom prefix logging
def log_with_prefix(prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix} Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 7. Delay execution
def delay(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Waiting {seconds} seconds...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 8. Custom header and footer
def add_banner(header, footer):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(header)
            result = func(*args, **kwargs)
            print(footer)
            return result
        return wrapper
    return decorator

# 9. Warn if execution exceeds n seconds
def warn_if_slow(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            if elapsed > threshold:
                print(f"⚠️ Warning: {func.__name__} took {elapsed:.2f}s (limit: {threshold}s)")
            return result
        return wrapper
    return decorator

# 10. Apply function to result
def transform_result(transform_func):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return transform_func(result)
        return wrapper
    return decorator

# -------------------------------
# Example Usage
# -------------------------------

@repeat_output(3)
def greet():
    return "Hi!"

@log_to_file("log.txt")
def add(a, b):
    return a + b

@limit_calls(2)
def limited():
    print("Called limited function")

@require_role("admin")
def delete_user(user):
    print(f"{user['name']} deleted something")

@min_arg_length(4)
def echo(text):
    print(text)

@log_with_prefix("[INFO]")
def action():
    print("Doing something...")

@delay(2)
def wait_and_print():
    print("Delayed task executed")

@add_banner("=== START ===", "=== END ===")
def say_hello():
    print("Hello World")

@warn_if_slow(1)
def long_task():
    time.sleep(1.5)
    print("Finished slow task")

@transform_result(lambda x: x * 2)
def get_value():
    return 10

# -------------------------------
# Run Tasks
# -------------------------------
if __name__ == "__main__":
    print(greet())
    print(add(3, 4))
    limited(); limited(); limited()  # 3rd call will be blocked
    delete_user({'name': 'Alice', 'role': 'admin'})
    delete_user({'name': 'Bob', 'role': 'guest'})
    echo("Test")
    echo("Yes")
    action()
    wait_and_print()
    say_hello()
    long_task()
    print("Transformed Result:", get_value())
