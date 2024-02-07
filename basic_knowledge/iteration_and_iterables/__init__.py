"""
Comprehensions
-> Concise syntax for describing lists, sets, and dictionaries.
-> Readable and expressive.
-> Close to natural language.
"""

"""
Iteration Protocols:
---------------------
iterable: 
-> Can be passed to iter() to produce an iterator

iterator:
-> Can be passed to next() to get the next value in the sequence
"""

"""
Laziness and the infinite
-> Generators only do enough work to produce requested data.
-> This allows generators to model infinite ( or just very large) sequences.
-> Examples of such sequences are:
    -> Sensor readings
    -> Mathematical sequences 
    -> Contents of large files
"""

"""
Summary:
-> Comprehensions for list, set, and dict
-> Comprehensions use an input iterable and optional predicate
-> Iterable objects can be iterated item by item
-> Use iter() to get an iterable from an iterable object
-> Use next() to get the next item from an iterable
-> Iterators raise StopIteration when they're exhausted
-> Generator functions describe sequences imperatively
-> Generator functions contain at least one yield
-> Generators are iterators
-> Each call to a generator function produces a new generator
-> Generators maintain explicit internal state
-> Generators yield values lazily
-> Built-in iteration tools include sum(), any(), and zip()
-> The itertools module includes many other tools for iteration
"""
