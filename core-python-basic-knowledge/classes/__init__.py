"""
Classes
-> Define the structure and behavior of objects.
-> Act as template for creating new objects.
-> Classes control an object's initial state, attributes, and methods.
"""

"""
__init__()
-> Instance method for initializing new objects
-> __init__() is an initializer, not a constructor
"""

"""
Class invariants 
Truths about an object that endure for its lifetime.
"""

"""
Polymorphism
Using objects of different types through a uniform 
interface.
It applies to both functions as well as more complex types.
"""

"""
Summary: 
-> All types in Python have a class
-> Classes define the structure and behavior of objects
-> An object's class is set when it's created, and it's fixed for the object's lifetime
-> Classes are a key part of object-oriented programming in Python
-> Classes are defined with the class keyword
-> Instances of a class are created by calling the class like a function
-> Instance methods are function defined within a class and must accept a self argument
-> Methods are called using the instance.method() syntax
-> Class may have a __init__() method for initializing new instances
-> A class's constructor will call __init__() if it's present
-> __init__() is not, strictly speaking, a constructor 
-> Arguments passed to the constructor are forwarded to __init__()
-> Instance attributes are created simply by assigning to them
-> Implementation details are conventionally prefixed with an underscore
-> Access to implementation details outside a class can be useful during development
-> Class invariants should be established within __init__() 
-> Methods and Classes can have docstrings
-> Method calls on self within a method must be preceded with self
-> A module can contain as many classes and functions as you wish
-> Polymorphism in Python is achieved through duck-typing
-> Polymorphism in Python doesn't rely on shared base classes or interfaces
-> Class inheritance in Python is primarily useful for sharing implementation 
-> All methods - including special methods - are inherited
-> 
"""
