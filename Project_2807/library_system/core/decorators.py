def admin_only(func):
    def wrapper(*args, **kwargs):
        user = input("Enter admin password: ")
        if user == "admin123":
            return func(*args, **kwargs)
        else:
            print("Access Denied. Admins only.")
    return wrapper
