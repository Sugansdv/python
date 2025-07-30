def dry_run_decorator(func):
    def wrapper(directory, dry=False):
        gen = func(directory)
        for message in gen:
            print(message)
            if not dry:
                # Trigger the generator's side effects
                pass
    return wrapper
