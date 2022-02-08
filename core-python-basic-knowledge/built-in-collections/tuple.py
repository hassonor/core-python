# tuple - Immutable sequences of arbitrary objects
t = ("Israel", 5.3, 3)
print(t)

t = t + (3381.0, 256e9)
print(t)

a = ((220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368))

k = (391,)

e = ()

p = 1, 1, 1, 4, 6, 19


def minmax(items):
    return min(items), max(items)


minmax([83, 33, 84, 32, 85, 31, 86])

lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])

a = "Or"
b = "Hasson"
a, b = b, a

print(tuple([561, 1105, 1729, 2465]))

print(tuple("Hasson"))

print(5 in (3, 5, 17, 22))
print(5 not in (3, 5, 17, 22))

"""
Summary:
-> Tuples are immutable sequences
-> Tuple literals are optional parentheses around comma-separated items
-> Use a trailing comma for single-element tuples
-> Tuple unpacking is useful for multiple return values and swapping
"""
