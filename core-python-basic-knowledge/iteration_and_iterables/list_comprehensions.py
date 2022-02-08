"""
List Comprehension Syntax:
[expr(item) for item in iterable]
"""
from math import factorial

f = [len(str(factorial(x))) for x in range(20)]
print(f)

words = "Why sometimes I have believed as many as six impossible things before berekfast".split()
print(words)

print([len(word) for word in words])
