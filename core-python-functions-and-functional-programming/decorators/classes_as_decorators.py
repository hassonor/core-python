"""
Classes as Decorators
1. Classes are callable objects
2. Functions decorated with a class are replaced by an instance of the class
3. These instances must themselves be callable

We can decorate with a class as long as instances of the class implement __call__().
"""


class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello, {}!'.format(name))


hello('Or')
hello('Ella')
hello('Shira')

print(hello.count)
