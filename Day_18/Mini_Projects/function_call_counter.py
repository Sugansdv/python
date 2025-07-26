import functools

def call_counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"[CALL COUNT] {func.__name__} called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0

    def reset():
        wrapper.calls = 0
        print(f"[RESET] {func.__name__} counter reset")

    wrapper.reset = reset
    return wrapper

@call_counter
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    greet("Alice")
    greet("Bob")
    greet.reset()
    greet("Charlie")
