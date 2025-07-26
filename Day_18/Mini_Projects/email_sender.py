import time
import random
import functools
from datetime import datetime

# Logging decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            result = func(*args, **kwargs)
            print(f"[{timestamp}] ✅ {func.__name__} succeeded with args={args}, kwargs={kwargs}")
            return result
        except Exception as e:
            print(f"[{timestamp}] ❌ {func.__name__} failed with args={args}, kwargs={kwargs} | Error: {e}")
            raise
    return wrapper

# Retry decorator
def retry(max_retries=2, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts <= max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Retry {attempts}/{max_retries} for {func.__name__}")
                    if attempts > max_retries:
                        print(f"❌ Max retries exceeded for {func.__name__}")
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

# Simulated email sender
@retry(max_retries=2, delay=1)
@log
def send_email(to_address, subject, message):
    # Simulate random failure
    if random.random() < 0.5:
        raise ConnectionError("Simulated network error")
    print(f" Email sent to {to_address}: {subject}")
    return "Success"

if __name__ == "__main__":
    try:
        send_email("user@example.com", "Hello", "This is a test email.")
    except Exception as e:
        print(f"Final Status: FAILED - {e}")
