import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Executed '{func.__name__}' in {duration:.4f}s")
        return result
    return wrapper
