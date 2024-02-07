"""
<<<<<<<<< What is a Context Manager? >>>>>>>>>>>>>>>>
-> An object designed to be used in a with statement.

<<<<<<<<<<<Methods around a Context>>>>>>>>>>>>>>>>>>
-> A context manager implements two methods.
-> The first is called before entering the with-block.
-> The second is called after exiting the with-block.

<<<<<<<<<< Context Manager Methods >>>>>>>>>>>>>>>>>>
    setup                     teardown
    construction              destruction
    allocation                deallocation
      enter                     exit


<<<<<<<<<<<<<< Context manager >>>>>>>>>>>>>>>>>>>>>>
-> An object that ensures that resources are properly and
automatically handled.
-> The "enter" method ensures that the resources is ready for use.
-> The "exit"  method ensures that the resource is cleaned up.


with expression: (-> Must evaluate to a context manager)
    with-block

"""

"""
Summary:
-> Context managers are objects that have both __enter__ and __exit__ methods.
-> The main use of context managers is for properly managing resources.
-> The expression in a with-statement must evaluate to a context manager object.
-> A with-statement calls its context manager's __enter__ method before entering the with-block.
-> The return value of __enter__ is bound to the as-variable of the with-statement, 
if it's defined.
-> __exit__ is called after the with-block is complete.
-> if the with-block exits with an exception, the exception is passed to __exit__
-> __exit__ can control the propagation of exception by return False to propagate it or True to swallow it.
-> The with-statement is syntactic sugar for a much larger and more complicated body of code.
"""
