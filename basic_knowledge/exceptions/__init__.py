"""
Exceptions Can Not Be Ignored
-> Error coded are easy to ignore
-> Checks are always required
"""

"""
Use Standard Exception Types
-> Standard types: Python provides standard exceptions types for signalling common errors.
-> Invalid argument values: Use ValueError for arguments of the right type but with an invalid value
-> Exception constructors: Use raise ValueError() to raise a new ValueError
"""

"""
Exceptions and Protocols
-> Sequences should raise IndexError for out-of-bounds indexing.
-> Exceptions must be implemented and documented correctly.
-> Existing built-in exceptions are ofter the right ones to use.
"""

"""
Summary:
-> Raising an exception interrupts program flow.
-> Handle exceptions with try...except
-> Exceptions can be detected within try-blocks
-> Except-blocks define handlers for exceptions
"""
