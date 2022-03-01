"""
<<<<< contextlib >>>>>
-> Standard library module that "provides utilities for common tasks involving the with statement"

<< The contextmanager Decorator >>
-> contextmanager is a decorator for creating new context managers.
 **** Concept ****
 -> To use contextmanager we first create a generator.
 -> Decorate the generator with contextmanager to create a context manager factory function.

<<< Benefits of Generators >>>>
-> Using a generator avoids the need to break context manager logic across two methods.
-> Since generators remember their state, they can be used to implement statement context
managers.

<<< Exception Propagation >>>>
-> Use normal exception handling to control exception propagation.
-> Re-raising or not catching an exception will propagate iot out of the with-statement.
-> Catching and not re-raising it will not propagate the exception.
-> Since we did not re-raise the ValueError it's not propagated out of the with-statement.

contextmanager is a very useful tool that simplifies the creation of most context managers.
"""

"""
Summary:
-> contextlib provides the contextmanager decorator.
-> contextmanager create context managers from generators.
-> Everything before the yield is part of the __enter__().
-> Exceptions are dealt with using normal exception handling tools.
"""
