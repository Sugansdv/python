import functools

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print("[CACHE HIT]")
            return cache[args]
        print("[CACHE MISS]")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def slow_add(x, y):
    from time import sleep
    sleep(2)
    return x + y

if __name__ == "__main__":
    print(slow_add(3, 4))
    print(slow_add(3, 4))  # Fast due to cache
