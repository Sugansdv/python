import random
import string
from core.utils import exclude_similar

@exclude_similar
def generate_password(length=12, pool=None):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")

    if pool is None:
        pool = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    password = "".join(random.choice(pool) for _ in range(length))
    return password

def infinite_passwords(length=12, exclude_similar=True):
    while True:
        yield generate_password(length=length, pool=None if exclude_similar else list(string.printable))
