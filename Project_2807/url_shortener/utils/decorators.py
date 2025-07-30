from functools import lru_cache

def cache(func):
    return lru_cache(maxsize=32)(func)
