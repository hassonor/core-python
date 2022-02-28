"""
Custom Exception
-> Domain-specific: Define a new TriangleError exception to be more explicit about the error.
-> Inheritance: The new exception should inherit from Exception, not BaseException
->  You should almost always specify an exception type in an except statement.
"""
"""
Exception Hierarchy
-> Exceptions are arranged into an inheritance hierarchy.
-> This facilitates catching exceptions by their base classes.

Related Exceptions
-> Similar purpose: Both exceptions communicate that a requested value doesn't exist.
-> Inheritance: We can explore their inheritance graphs to see if they're related.
-> __mro__: We can use their method resolution orders as way to see their inheritance graphs.

*** We can catch both IndexError and KeyError by catching LookupError.
"""

"""
The Practicality Of OSError
-> OSError tells us that something has gone wrong with a filesystem operation.
-> Often It's not necessary to know the details of exactly what went wrong.
-> Even when you catch the general exception type, the details are still available.
"""
