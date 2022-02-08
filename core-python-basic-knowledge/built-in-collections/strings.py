# Strings
"""
Strings are immutable. You can not modify them in place.

Use str.join() to Join Strings
1. Concatenation with + results in temporaries
2. str.join() inserts a separator between a collection of strings
3. Call join() on the separator string
"""

len("OrHasson")
colors = ';'.join(['#1234', '#1234', '#1234', '#1234', '#1234'])
print(colors)

colors.split(';')
print(colors)

print(''.join(['Or', 'Hasson']))

print("unforgetable".partition('forget'))

departure, separator, arrival = "Tel-Aviv:Tokyo".partition(':')
print(departure)
print(separator)
print(arrival)

origin, _, destination = "Tel-Aviv:New-York".partition(':')
print(origin)
print(destination)

# String formatting
print("{0} north {1} east".format(10, 30))

print("The formatting order is like the string {} and the string {}".format("this1", "this2"))

print("Galactic position x={pos[0]}, y={pos[0]},z={pos[0]}".format(pos=(1, 2, 3)))

import math

print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))

import datetime

print(f"The current time is {datetime.datetime.now().isoformat()}.")

# Range
"""
Sequence representing an arithmetic progression of integers
"""

print(list(range(5, 10)))
print(list(range(0, 10, 2)))  # step of 2

"""
enumerate:
Constructs an iterable of (index, value) tuples around another iterable object
"""

t = [10, 12, 15, 312321, 123123312]

for index, value in enumerate(t):
    print(f"i={index}, v = {value}")

str_to_arr = "HelloWorld"
print(list(str_to_arr))

"""
Summary:
-> Use str.join() for efficient string concatenation.
-> Use str.partition() for certain simple string parsing operations.
-> str.format() is a powerful string interpolation technique.
-> f-strings are a kind of string literal for performing interpolation.
-> range() can be called with one,two, or three arguments: start, stop and step.
-> enumerate is ofter better than range for making loop counters.
"""
