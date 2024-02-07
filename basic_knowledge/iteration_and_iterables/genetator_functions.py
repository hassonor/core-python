"""
Generator Functions
-> Iterables defined by functions
-> Lazy evaluation
-> Can model sequences with no definite end
-> Composable into pipelines

yield:
-> Generator functions must include at lease one yield statement.
-> They may also include return statements.
"""


def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()
print(next(g))
print(next(g))
print(next(g))

for v in gen123():
    print(v)


def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")


g = gen246()
print(next(g))
