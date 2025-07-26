import functools

def validate_types(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, exp_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, exp_type):
                    raise TypeError(f"Arg {i + 1} must be {exp_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_types(int, int)
def add(x, y):
    return x + y

@validate_types(str, str)
def concat(a, b):
    return a + b

if __name__ == "__main__":
    print(add(3, 4))
    print(concat("Hello", "World"))
