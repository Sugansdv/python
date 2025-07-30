from functools import wraps

_cache = {}

def cache_rates(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "rates" in _cache:
            return _cache["rates"]
        result = func(*args, **kwargs)
        _cache["rates"] = result
        return result
    return wrapper
