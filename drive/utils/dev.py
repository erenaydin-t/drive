from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f" {te - ts:2.4f} s: func:{f.__name__!r} ")
        return result

    return wrap
