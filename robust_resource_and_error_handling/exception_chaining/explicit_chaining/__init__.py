"""
Explicit chaining:
-> Deliberately associate an exception with a new exception at the point or raising the latter.
-> This is done to translate one exception to another.

-> When translating exceptions, consider whether to use explicit exception chaining.

<<<<<<<< Explicit Exception Chaining >>>>>>>>>>
except <original exception type> as e:
    raise <new exception> from e

Associates new exception with original exception through the __cause__ attribute
"""
