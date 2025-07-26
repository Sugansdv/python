import functools
import random

# --- Decorator: Alert on threshold breach ---
def alert_on_anomaly(threshold):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f" ALERT: {func.__name__} result {result} exceeds threshold of {threshold}!")
            else:
                print(f"[OK] {func.__name__} result: {result}")
            return result
        return wrapper
    return decorator

# --- Simulated Sensor Data Function ---
@alert_on_anomaly(threshold=75)
def read_temperature_sensor():
    # Simulate temperature between 50 and 100
    return random.uniform(50, 100)

@alert_on_anomaly(threshold=50)
def read_humidity_sensor():
    # Simulate humidity between 30 and 70
    return random.uniform(30, 70)

if __name__ == "__main__":
    print("\n Reading sensors...\n")
    for _ in range(5):
        read_temperature_sensor()
        read_humidity_sensor()
        print("-" * 40)
