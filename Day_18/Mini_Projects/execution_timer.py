import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timeit
def compute():
    time.sleep(1.5)
    return "Done"

if __name__ == "__main__":
    compute()
