import functools

# --- Parameterized Decorator ---
def html_wrapper(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return f"<{tag}>{content}</{tag}>"
        return wrapper
    return decorator

@html_wrapper("div")
@html_wrapper("h1")
@html_wrapper("p")
def get_welcome_message():
    return "Welcome to the HTML Decorator Demo!"

@html_wrapper("section")
@html_wrapper("h2")
def get_subheader():
    return "This is a subheading."


if __name__ == "__main__":
    print(" HTML Output 1:")
    print(get_welcome_message())
    print("\n HTML Output 2:")
    print(get_subheader())
