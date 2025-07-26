import time
import functools
from collections import deque

def throttle(limit_per_minute):
    def decorator(func):
        call_times = deque()  # store timestamps of recent calls

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            # Remove timestamps older than 60 seconds
            while call_times and current_time - call_times[0] > 60:
                call_times.popleft()

            if len(call_times) >= limit_per_minute:
                print(f"[THROTTLED] Function '{func.__name__}' blocked. Limit of {limit_per_minute} calls/minute exceeded.")
                raise Exception(f"Rate limit exceeded: {limit_per_minute} calls per minute allowed.")
            
            call_times.append(current_time)
            return func(*args, **kwargs)

        return wrapper
    return decorator

# Example usage
@throttle(5)  # allow max 5 calls per minute
def fetch_data():
    print(f"[SUCCESS] Data fetched at {time.strftime('%X')}")


if __name__ == "__main__":
    for i in range(7):  # Try calling 7 times
        try:
            fetch_data()
        except Exception as e:
            print("", e)
        time.sleep(5)  # wait 5 seconds between calls
