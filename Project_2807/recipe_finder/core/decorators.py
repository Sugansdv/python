from datetime import datetime

def log_search(func):
    def wrapper(*args, **kwargs):
        ingredient = args[1]
        print(f"[{datetime.now()}] Searching for recipes with: '{ingredient}'")
        return func(*args, **kwargs)
    return wrapper
