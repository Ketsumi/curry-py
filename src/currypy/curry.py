from functools import partial
from inspect import signature

def curry(f):

    def wrapper(*args):
        if len(args) >= len(signature(f).parameters):
            return f(*args)

        return curry(partial(f, *args))

    return wrapper
