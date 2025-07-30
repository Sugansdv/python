from functools import wraps

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(self, student):
        if student.id in cache:
            return cache[student.id]
        result = func(self, student)
        cache[student.id] = result
        return result

    return wrapper
