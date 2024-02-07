"""
Decorators Mechanics
-> Decorators take a callable argument and return a callable
-> In this example, the callable we return is the local function wrap()
-> wrap() uses a closure to access f after escape_unicode() returns
"""


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def northern_city():
    return "Ør HassØn"


print(northern_city())
