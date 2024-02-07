import socket
from resolver import Resolver
from timeit import timeit


def resolve(host):
    return socket.gethostbyname(host)


print(resolve('google.com'))

"""
__call__()
-> Allows instances of classes to be callable objects.
-> __call()__ is invoked on objects when they are called like functions.
"""

resolve = Resolver()
print(resolve('google.com'))
print(resolve.__call__('google.com'))  # This is really just syntactic sugar for calling __call__ directly.

print(resolve.cache)

resolve('mako.co.il')
print(resolve.cache)

# without cache
print(timeit(setup="from __main__ import resolve", stmt="resolve('gmail.com')", number=1))

# after first call we have it in the cache
# with cache
print(timeit(setup="from __main__ import resolve", stmt="resolve('gmail.com')", number=1))

resolve2 = Resolver()
print(resolve2.has_host("google.com"))  # False

resolve2("mako.co.il")
print(resolve2.has_host("mako.co.il"))  # True
