from functools import wraps
from datetime import datetime

def log_encryptions(func):
    @wraps(func)
    def wrapper(self, file_path, *args, **kwargs):
        action = "ENCRYPTED" if "encrypt" in func.__name__ else "DECRYPTED"
        result = func(self, file_path, *args, **kwargs)
        with open("encryption_log.txt", "a") as log:
            log.write(f"{datetime.now()} - {action} - {file_path}\n")
        return result
    return wrapper
