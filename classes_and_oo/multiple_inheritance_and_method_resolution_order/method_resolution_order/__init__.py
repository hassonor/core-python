"""
<<<<<<<<<<<<<<< Method Resolution Order (MRO) >>>>>>>>>>>>>>>
-> Ordering of an inheritance graph that determines which implementation to use when invoking a method.
-> Method implementation may be found in any class in an inheritance graph
-> Determines the order in which the graph is searched when looking for an implementation

<<<<<<<<<<<<<<<<<<< How is MRO Used? >>>>>>>>>>>>>>>>>>>>>>>>>>>>
-> Python finds the MRO for the type of the object on which a method is invoked.
-> Python checks each class in the MRO in order to find one that implements the method.
-> The first implementation found is used.
"""

"""
<< object >>
The ultimate base class for every class in Python.
"""

"""
<< C3 >>
Algorithm used to calculate method resolution orders
Ensures that:
 -> Subclasses come before base classes
 -> Base class order from class definition is preserved
 -> The first two qualities are preserved for all MROs in a program
 
"""
