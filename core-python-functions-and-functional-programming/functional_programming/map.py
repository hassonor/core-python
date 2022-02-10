"""
map()
-> Calls a function for the elements in a sequence,
producing a new sequence with the return values
-> It "maps" a function over a sequence

map() Is Lazy
-> map() will not call its function or access its iterables until they're needed for output
-> A map object is itself iterable; iterate over it to produce output
"""
import itertools


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


result = map(Trace()(ord), 'The quick brown fox')
print(result)
print(next(result))

print(list(map(ord, 'The quick brown fox')))

for o in map(ord, 'The quick brown fox'):
    print(o)

# map() with Multiple Iterables
sizes = ['small', 'medium', 'large']
colors = ['lavender', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']


def combine(size, color, animal):
    return '{} {} {}'.format(size, color, animal)


print(list(map(combine, sizes, colors, animals)))


def combine_2(quantity, size, color, animal):
    return '{} x {} {} {}'.format(quantity, size, color, animal)


print(list(map(combine_2, itertools.count(), sizes, colors, animals)))

# map() and Comprehensions
print([str(i) for i in range(5)])  # -> ['0','1','2','3','4']

print(list(map(str, range(5))))  # -> ['0','1','2','3','4']

i = (str(i) for i in range(5))
print(list(i))  # -> ['0','1','2','3','4']

i = map(str, range(5))
print(list(i))  # -> ['0','1','2','3','4']
