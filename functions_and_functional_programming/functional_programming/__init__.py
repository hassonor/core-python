"""
Summary:
-> map() applies a callable to each element in a sequence
-> map() produces its results lazily
-> map() can accept multiple input iterables

-> filter() applies a predicate to the elements of an iterable
-> It produces an iterable containing the input elements for which the predicate returned True

-> functools.reduce()
    -> Repeatedly applies a two-argument callable to accumulate the elements in an iterable.
    -> Raises an exception on empty input iterables
    -> You can provide an initial value to avoid this issue
    -> Selecting the right initial value is crucial
    -> Combining map() and reduce() to make map-reduce
"""
