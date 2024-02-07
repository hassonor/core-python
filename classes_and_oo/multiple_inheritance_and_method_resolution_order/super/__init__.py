"""
<<<<< super() >>>>>
Given a method resolution order and a class C in that
MRO, super() gives you an object which resolves methods using only the part of the MRO which comes after C.

super() works with the MRO of an object, not just its base classes.

super() gives you a proxy object
-> The proxy resolves the correct implementation if any requested method.
-> It has access to the entire inheritance graph of the object.

super() uses the full MRO of an object, not just the base classes from a class definition.

"""
