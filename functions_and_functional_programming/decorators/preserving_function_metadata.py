"""
functools.wraps()
-> Replace decorator metadata with that of the decorated callable.
-> It is a decorator that you apply to your wrapper function.
"""

import functools


def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()

    return noop_wrapper


@noop
def hello():
    "Print a well-known message."
    print('hello world!')


hello()
print(hello.__name__)
print(hello.__doc__)
