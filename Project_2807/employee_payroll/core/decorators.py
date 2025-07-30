def admin_only(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get('is_admin', False):
            print("Access denied: Admins only.")
            return
        return func(*args, **kwargs)
    return wrapper
