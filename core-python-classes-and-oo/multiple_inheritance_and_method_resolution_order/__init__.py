"""
<<<<<<<<<< Summary >>>>>>>>>>>
-> Use a comma-separated list of class names multiple base classes
-> A class can have as many base classes as you want
-> You should generally explicitly initialize base classes
-> Python will call, ast most, the initializer of the first of multiple base class.
-> Python will call a base class initializer only if the subclass doesn't define one.
-> __bases__ is a tuple defining the base classes for the class
-> __bases__ is in the same order as in the class definition
-> __bases__ is populated for both single and multiple inheritance
-> Method resolution order is the order in which Python searches an inheritance graph
-> MRO is a tuple of types in the __mro__ attribute
-> Python uses the first entry in an MRO which has the method
-> MRO is dependent on base class declaration order
-> MRO is calculated by Python using the C3 algorithm
-> C3 preserves base-class declaration order
-> C3 puts subclasses before base classes
-> It is possible to specify an inconsistent base class ordering
-> super() uses the elements in an MRo after some specified type
-> super() returns a proxy object
-> A super proxy uses a subset of an MRo for name resolution
-> You can't directly call instance methods on class-bound proxies
-> Inappropriate use of super() can violate design constraints
-> Classes can be designed to cooperate without a priori knowledge of one another
-> object is at the core of Python's object model
-> object is the ultimate base class for all other classes
-> Python will automatically provide object as a base class
-> object provides default implementations of many common Python methods
-> object implements the core attribute functionality in Python
-> Inheritance in Python is best used as a way to share implementation
"""
