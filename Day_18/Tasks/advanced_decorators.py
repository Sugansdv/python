import time
from functools import wraps
import hashlib
from cryptography.fernet import Fernet
import base64

# Helper for encryption key (simulate a key generator based on password)
def generate_key_from_password(password: str):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# 1. API rate limit (5 calls per 60 seconds)
def rate_limit(max_calls=5, period=60):
    call_times = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove old timestamps
            while call_times and now - call_times[0] > period:
                call_times.pop(0)

            if len(call_times) >= max_calls:
                print(f"[RATE LIMIT] Max {max_calls} calls per {period}s reached. Try later.")
                return None

            call_times.append(now)
            return func(*args, **kwargs)

        return wrapper
    return decorator

# 2. Retry failed function up to 3 times
def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"[RETRY] Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed attempt {attempt}: {e}")
                    if attempt == max_attempts:
                        raise
                    time.sleep(1)
        return wrapper
    return decorator

# 3. Time tracking
call_times_log = []

def track_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = round(time.time() - start, 4)
        log_entry = f"{func.__name__} took {elapsed} sec"
        call_times_log.append(log_entry)
        print(f"[TIME TRACK] {log_entry}")
        return result
    return wrapper

# 4. Security: check API token
VALID_TOKEN = "abc123token"

def require_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get("token")
        if token != VALID_TOKEN:
            print("[SECURITY] Invalid or missing API token.")
            return None
        return func(*args, **kwargs)
    return wrapper

# 5. Encrypt/Decrypt return values
def encrypt_result(password):
    key = generate_key_from_password(password)
    fernet = Fernet(key)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, str):
                raise ValueError("Only string return values can be encrypted.")
            encrypted = fernet.encrypt(result.encode()).decode()
            print(f"[ENCRYPTED]: {encrypted}")

            # simulate decrypt (for demo purposes)
            decrypted = fernet.decrypt(encrypted.encode()).decode()
            print(f"[DECRYPTED]: {decrypted}")
            return decrypted

        return wrapper
    return decorator

# =========================
# Example Usages
# =========================

@rate_limit()
def task1():
    print("API call executed.")

@retry(3)
def task2():
    print("Trying risky task...")
    raise ValueError("Temporary failure")

@track_time
def task3():
    time.sleep(0.2)
    print("Tracked task complete")

@require_token
def task4(data, token=None):
    print(f"Secure data access: {data}")

@encrypt_result("my-secret-password")
def task5():
    return "Sensitive Information"

# =========================
# Run All Tasks
# =========================
if __name__ == "__main__":
    print("\n1. Rate Limit")
    for _ in range(7):  # 2 calls should get blocked
        task1()
        time.sleep(0.5)

    print("\n2. Retry")
    try:
        task2()
    except Exception:
        print("All retry attempts failed.")

    print("\n3. Track Time")
    task3()
    print("Log:", call_times_log)

    print("\n4. Require Token")
    task4("Confidential", token="wrongtoken")  # blocked
    task4("Confidential", token="abc123token")  # allowed

    print("\n5. Encrypt/Decrypt")
    task5()
