import time
from functools import wraps

def snooze(delay=300):  # 5 minutes by default
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Snooze activated. Alarm will go off again in 5 minutes.")
            time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator
