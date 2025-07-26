import functools

def remove_nulls(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item for item in data if item is not None]
        return func(cleaned)
    return wrapper

def strip_whitespace(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item.strip() for item in data if isinstance(item, str)]
        return func(cleaned)
    return wrapper

def to_lowercase(func):
    @functools.wraps(func)
    def wrapper(data):
        cleaned = [item.lower() for item in data if isinstance(item, str)]
        return func(cleaned)
    return wrapper

@remove_nulls
@strip_whitespace
@to_lowercase
def clean_data(data):
    return data

if __name__ == "__main__":
    raw = ["  Apple  ", None, " BANANA", "OrAnGe  ", "", None]
    print(clean_data(raw))
