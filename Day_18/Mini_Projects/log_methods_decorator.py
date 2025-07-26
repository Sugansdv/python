import functools

# --- Class Decorator ---
def log_methods(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            original_method = attr_value

            @functools.wraps(original_method)
            def logged_method(self, *args, __method=original_method, **kwargs):
                print(f"[LOG] Calling: {__method.__name__} | Args: {args} | Kwargs: {kwargs}")
                return __method(self, *args, **kwargs)

            setattr(cls, attr_name, logged_method)
    return cls

@log_methods
class Calculator:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def power(self, base, exp=2):
        return base ** exp

if __name__ == "__main__":
    calc = Calculator()
    print("Result:", calc.add(5, 3))
    print("Result:", calc.multiply(2, 4))
    print("Result:", calc.power(2))
    print("Result:", calc.power(2, exp=5))
