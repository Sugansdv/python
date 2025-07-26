import functools
from datetime import datetime

def file_log(level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open("log.txt", "a") as f:
                f.write(f"[{datetime.now()}] [{level}] {func.__name__} -> {result}\n")
            return result
        return wrapper
    return decorator

@file_log(level="DEBUG")
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    print(greet("Alice"))
