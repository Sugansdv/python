import functools

# Simulated global user object
user = {
    "name": "John",
    "is_logged_in": False  # Change to True to simulate login
}

# Decorator to enforce login
def require_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user.get("is_logged_in"):
            raise Exception("Authentication required")
        return func(*args, **kwargs)
    return wrapper

# Example protected function
@require_login
def access_dashboard():
    print(f"Welcome to your dashboard, {user['name']}!")
    return "Dashboard loaded"


if __name__ == "__main__":
    try:
        result = access_dashboard()
        print("Result:", result)
    except Exception as e:
        print(" Error:", e)
