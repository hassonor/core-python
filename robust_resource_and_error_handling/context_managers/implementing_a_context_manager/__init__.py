"""
<<>> __enter__() <<>>
-> Called on a context manager just before entering the with-block
-> The return value is bound the as-variable.
-> May return any value it wants, including None.
-> Commonly returns the context manager itself.

<<>> __exit__() <<>>
-> Executed after the with-block terminates
-> Handles exceptional exits from the with-block
-> It receives the exception type, value, and traceback
-> The arguments are None when there is no exception
-> By default, __exit__() will propagate exceptions from the with-block to the
enclosing context.
-> if __exit__() returns a "falsy" value,
exceptions will be propagated.
-> if answers the question "Should I swallow exception?"
-> By default it propagates exceptions
-> This is because functions return None by default

<<< Exception Response >>>
-> __exit__() often needs to choose an action based on whether an exception was raised.


<<< Raising Exceptions in __exit__() >>>
-> __exit__() should not re-raise the exception is receives from the with-block.
-> To ensure that the exception is propagated, simply return False.
-> __exit__() should only raise an exception if something goes wrong in the function itself.


"""
