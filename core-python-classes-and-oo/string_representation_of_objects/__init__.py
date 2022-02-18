"""
Overriding __repr__()

-> The default __repr__ inherited from object is not much use.
-> Override __repr__ to return a more useful string, which ideally formatted as source
code for a constructor call. (see position __repr__ examaple).
"""

"""
Summary:
-> repr() gives a string for developers 
-> str() - the string constructor - gives a string for users
-> format() gives more control

-> repr(obj) delegated to obj.__repr__()
-> str(obj) delegated to obj.__str__()
-> format(obj, spec) delegates to obj.__format__(spec)

-> All classes inherit default __repr__(), __str__() and __format__()
-> The default __repr__() isn't very helpful
-> Most classes should override __repr__()

"""
