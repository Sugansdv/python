import functools

def validate_token(required_token):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            token = kwargs.get("token")
            if token != required_token:
                print("[ACCESS DENIED] Invalid or missing token")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_token("secret_token")
def get_data(token=None):
    return {"data": "Top Secret"}

if __name__ == "__main__":
    print(get_data(token="wrong_token"))
    print(get_data(token="secret_token"))
