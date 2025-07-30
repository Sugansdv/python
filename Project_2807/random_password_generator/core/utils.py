import functools
import string

def exclude_similar(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pool = kwargs.get("pool")
        if pool is None:
            pool = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        # Remove similar characters
        similar_chars = {'l', '1', 'I', '0', 'O', 'o'}
        filtered_pool = [c for c in pool if c not in similar_chars]
        kwargs["pool"] = filtered_pool
        return func(*args, **kwargs)
    return wrapper
