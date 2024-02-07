# """Extended Call Syntax for Mappings"""
def color(red, green, blue, **kwargs):
    print("r = ", red)
    print("g = ", green)
    print("b = ", blue)
    print(kwargs)


"""
dict() uses **kwargs in its initializer.
we can use this in our previous example instead of a dict literal.
"""

k = {'red': 21, 'green': 68, 'blue': 120, 'alpha': 52}
print(color(**k))

k = dict(red=21, green=68, blue=120, alpha=52)

"""Argument Forwarding"""


def trace(f, *args, **kwargs):
    print("args =", args)
    print("kwargs = ", kwargs)
    result = f(*args, **kwargs)
    print("result = ", result)
    return result


trace(int, "ff", base=16)
