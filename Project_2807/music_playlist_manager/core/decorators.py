def repeat(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        while True:
            try:
                yield next(gen)
            except StopIteration:
                gen = func(*args, **kwargs)
    return wrapper
