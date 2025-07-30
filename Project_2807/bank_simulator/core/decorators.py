import functools
import datetime

def audit(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        log_entry = {
            "action": func.__name__,
            "amount": args[0] if args else None,
            "timestamp": str(datetime.datetime.now())
        }
        self.transactions.append(log_entry)
        return result
    return wrapper
