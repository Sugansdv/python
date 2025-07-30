def logged_in(func):
    def wrapper(self, *args, **kwargs):
        if not self.authenticated:
            print("Error: Not logged in.")
            return
        return func(self, *args, **kwargs)
    return wrapper
