"""
<<<<<< Multiple Context Managers >>>>>>>
-> with cm1() as a, cm2() as b:
    BODY

-> Any exception propagated from inner context managers will be seen by outer context managers.
-> If an inner context manager swallows an exception, it won't be seen by outer context managers.

*** DON'T PASS A SEQUENCE TO A WITH-STATEMENT *****
"""

"""
Summary:
-> With-statement accept multiple comma-separated context managers.
-> This is equivalent to nesting with-statements.
-> Exception propagate from inner to outer context managers. 
-> Avoid passing lists or other sequences to with-statements.
"""
