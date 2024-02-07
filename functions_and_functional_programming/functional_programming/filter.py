"""
filter()
-> Removes elements from a sequence which don't meet some criteria
-> Applies a predicate function to each element
-> Produces its results lazily
-> Only accepts a single input sequence, and the function must accept only one argument

-> Passing None as the first argument to filter() will filter out input element which evaluate to False
"""

positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
print(list(positives))

# Filtering with None
trues = filter(None, [0, 1, False, True, [], [1, 2, 3], '', 'hello'])
print(list(trues))
