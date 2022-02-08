"""
Generator Expressions
Syntax: (exp(item) for item in iterable)
"""

"""
To recreate a generator
from a generator expression, 
you must execute the expression again.
"""

"""
Optional Parentheses
func (expr(item) for item in iterable)
"""

million_squares = (x * x for x in range(1, 1000001))
print(list(million_squares))

print(sum(x * x for x in range(1, 10000001)))

print(sum(x * x for x in range(1001) if x < 10))
