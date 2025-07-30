import functools

def log_chat(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        user_input = args[0]
        response = func(self, *args, **kwargs)
        with open("chat_log.txt", "a") as f:
            f.write(f"User: {user_input}\nBot: {response}\n\n")
        return response
    return wrapper
