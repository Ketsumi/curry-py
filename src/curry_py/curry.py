from functools import partial
from inspect import signature

def curry(f):

    def wrapper(arg):
        # print(len(signature(f).parameters))

        if len(signature(f).parameters) == 1:
            return f(arg)

        return curry(partial(f, arg))

    return wrapper
