from functools import wraps

# 1. Class-based decorator: log before and after
class LogExecution:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"[LOG] Starting: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"[LOG] Finished: {self.func.__name__}")
        return result

# 2. Memoization (caching) decorator
class Memoize:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            print(f"[CACHE] Hit for {args}")
            return self.cache[args]
        print(f"[CACHE] Miss for {args}")
        result = self.func(*args)
        self.cache[args] = result
        return result

# 3. Track how many instances created of a decorated class
class CountInstances:
    def __init__(self, cls):
        self.cls = cls
        self.count = 0
        wraps(cls)(self)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"[INSTANCE COUNT] Created {self.count} instance(s) of {self.cls.__name__}")
        return self.cls(*args, **kwargs)

# 4. @classmethod with custom logger
class ClassMethodLogger:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __get__(self, instance, owner):
        @classmethod
        @wraps(self.func)
        def wrapper(cls, *args, **kwargs):
            print(f"[CLASS LOG] Calling {self.func.__name__} from {cls.__name__}")
            return self.func(cls, *args, **kwargs)
        return wrapper.__get__(instance, owner)

# 5. Combine @property with custom decorator
class PropertyLogger:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __get__(self, instance, owner):
        print(f"[PROPERTY] Accessing {self.func.__name__}")
        return self.func(instance)

# ===============================
# Example Usages
# ===============================

# 1. LogExecution
@LogExecution
def greet(name):
    print(f"Hello, {name}!")

# 2. Memoize
@Memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3. CountInstances
@CountInstances
class Animal:
    def __init__(self, name):
        self.name = name

# 4. Class method with logger
class User:
    @ClassMethodLogger
    def get_user_info(cls, uid):
        return f"User ID: {uid}"

# 5. Property access logger
class Product:
    def __init__(self, name):
        self._name = name

    @PropertyLogger
    def name(self):
        return self._name

# ===============================
# Run All Tasks
# ===============================
if __name__ == "__main__":
    print("1. LogExecution")
    greet("Alice")

    print("\n2. Memoize")
    print("Fibonacci(5):", fibonacci(5))
    print("Fibonacci(5) again:", fibonacci(5))  

    print("\n3. CountInstances")
    a1 = Animal("Dog")
    a2 = Animal("Cat")

    print("\n4. ClassMethodLogger")
    print(User.get_user_info(101))

    print("\n5. PropertyLogger")
    p = Product("Laptop")
    print("Product name:", p.name)
