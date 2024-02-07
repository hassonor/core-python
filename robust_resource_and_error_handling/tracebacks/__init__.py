"""
Tracebacks: <<< __traceback__ >>>
-> Attribute on an exception object that holds a reference to the traceback object

-> traceback: Standard library module containing functions for working with traceback objects.
"""

"""
More Traceback Functions
-> There are many more functions in the traceback module
-> format_tb() can render a traceback to a string
"""

"""
Storing Tracebacks:
-> Rendering: Try to render a traceback within the scope of the except block
-> Stack frames: Tracebacks contain references to their stack frames and, thus, to all of the locals in
those frames.
-> Memory usage: The transitive closure over the stack frames can use a lot of memory, and it won't be garbage
collected until the traceback is released.
-> Transform: For longer term storage, render tracebacks into a different, more concise form suited to your needs.
"""
