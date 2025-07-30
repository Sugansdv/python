import time
from functools import wraps

def retry(max_attempts=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"[Retry {attempts}/{max_attempts}] Error: {e}")
                    time.sleep(delay)
            raise Exception("Failed after maximum retry attempts.")
        return wrapper
    return decorator
