from functools import wraps
from datetime import datetime

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Started at: {datetime.now()}")
        result = func(*args, **kwargs)
        print(f"Finished at: {datetime.now()}")
        return result
    return wrapper
