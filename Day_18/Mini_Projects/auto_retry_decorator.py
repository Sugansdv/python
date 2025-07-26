import time
import functools

def retry(max_retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    result = func(*args, **kwargs)
                    print(f"[SUCCESS] Attempt {attempts + 1}")
                    return result
                except Exception as e:
                    attempts += 1
                    print(f"[RETRY] Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            print("[FAILED] All retry attempts failed.")
        return wrapper
    return decorator

@retry(max_retries=3, delay=2)
def unreliable_func():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure!")
    return "Success!"

if __name__ == "__main__":
    print(unreliable_func())
