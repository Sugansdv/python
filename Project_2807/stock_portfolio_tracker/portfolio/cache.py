import functools

_cache = {}

def cache(func):
    @functools.wraps(func)
    def wrapper(*args):
        if args in _cache:
            print(f" Cached data for {args}")
            return _cache[args]
        result = func(*args)
        _cache[args] = result
        return result
    return wrapper
