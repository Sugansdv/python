import functools
import datetime
import random

def api_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            result = func(*args, **kwargs)
            status = "Success"
        except Exception as e:
            result = None
            status = f"Fail ({str(e)})"
        log_entry = (
            f"[{timestamp}] Function: {func.__name__}, "
            f"Args: {args}, Kwargs: {kwargs}, Status: {status}"
        )
        print(log_entry)
        return result
    return wrapper

# Simulated API call
@api_logger
def fetch_user_data(user_id):
    if random.choice([True, False]):  # Randomly succeed/fail
        return {"id": user_id, "name": "John Doe"}
    else:
        raise Exception("API request failed!")

# Simulate a few calls
if __name__ == "__main__":
    for i in range(5):
        print(fetch_user_data(i))
