"""
Instances as Decorators
-> Python calls an instance's __call__() when
it's used as a decorator
-> __call()'s return value is used as the new function
-> Create groups of callables that you can dynamically control as a group
"""


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


l = [1, 2, 3]
l = rotate_list(l)
print(l)

l = rotate_list(l)
print(l)

l = rotate_list(l)
print(l)

tracer.enabled = False
l = rotate_list(l)
print(l)
