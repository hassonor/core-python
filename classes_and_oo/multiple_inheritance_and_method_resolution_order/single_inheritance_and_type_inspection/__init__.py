"""
<<<<<<<<<<Base Class Initializers>>>>>>>>>>>
-> Unlike C++ and Java, Python doesn't automatically call base class initializers.
-> __init__ is treated just like any other method.
-> If a subclass defines __init__, it must explicitly call the base class implementation for it to be run.
"""

"""
<<<<<<<<<Type Inspection>>>>>>>>>>
isinstance()
------------------
Determines if an object is an instance of type.
Takes an object as its first arguments and a type as its second.
Returns True of the first arguments is an instance of the second.
examples:
-> print(isinstance(5, int) -> True
-> print(isinstance('Or Hasson!', str) -> True
-> print(isinstance(4.999, bytes) -> False

<<<<<<<<Checking Multiple Types>>>>>>>>>>>>>
isinstance(obj, (type_a, type_b, type_c))

"""

"""
<<<<<<<<<<Type Checks in Python>>>>>>>>>>>>>>
isinstance() can be used for type checking in Python
Some people consider type checking a sign of poor design. 
Sometimes they're the easiest way to solve a problem.
"""

"""
<<<<<<<< issubclass() >>>>>>>>>>
Operates on types to check for sub/superclass relationships.

Determines if one class is a subclass of another.

Takes two arguments, both of which must be types.

Returns True if the first argument is a subclass of the second.
"""
