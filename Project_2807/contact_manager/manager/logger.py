from functools import wraps
from datetime import datetime

def log_actions(func):
    """Decorator to log function calls with timestamp."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("data/log.txt", "a") as log_file:
            log_file.write(f"[{datetime.now()}] Called: {func.__name__}\n")
        return result
    return wrapper
