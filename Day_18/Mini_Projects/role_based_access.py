import functools
import datetime

# Simulated current user context
current_user = {
    "username": "john_doe",
    "role": "viewer"  # Try changing this to 'admin' or 'editor'
}

def access_control(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_role = current_user.get("role", "")
            if user_role != required_role:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] ACCESS DENIED: '{current_user['username']}' tried to access '{func.__name__}' (Required: {required_role}, Found: {user_role})")
                return f"Access Denied for user '{current_user['username']}'"
            return func(*args, **kwargs)
        return wrapper
    return decorator

# --- Usage Example ---

@access_control("admin")
def delete_user(user_id):
    return f"User {user_id} deleted."

@access_control("editor")
def edit_article(article_id):
    return f"Article {article_id} edited."

@access_control("viewer")
def view_dashboard():
    return "Dashboard Data"

# --- Simulated Calls ---
if __name__ == "__main__":
    print(delete_user(5))         # Access Denied if role != admin
    print(edit_article(3))        # Access Denied if role != editor
    print(view_dashboard())       # Should work if role == viewer
