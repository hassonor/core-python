"""
Scopes in Python
Local -> Inside the current function
Enclosing -> Inside enclosing functions
Global -> At the top level of the module
Built-in -> In the special builtins module

***********LEGB*************
"""

"""
@classmethod
-> Requires access to the class object to call other class methods or the constructor

@staticmethod
-> No access needed to either class or instance objects
-> Most likely an implementation detail of the class
-> May be able to be moved outside the class to become a global-scope function in the module
"""

"""
    The 'named constructor' idiom
A factory method which returns an instance of a class.
The method name allows callers to express intent, and 
allows construction to be performed with different combinations of the arguments.

"""

"""
Use **kwargs to thread
arguments through named-constructor class-methods to more
specialized subclasses.
"""

"""
Summary:
-> Use @staticmethod for methods which need neither the class nor the instance
-> Use @classmethod for methods which
-> Use @classmethod for the named-constructor idiom
-> Static- and class-methods can be overridden
-> Static- and class-methods are polymorphic when invoked through self
-> Use the @property decorator instead of getters and setters
-> Easily override properties by delegating to regular methods
"""
