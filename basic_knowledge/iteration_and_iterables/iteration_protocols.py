"""
Stopping Iteration with an Exception:
-> A single end: Sequences only have on ending, after all, so reaching it is exceptional
-> Infinite sequences: Finding the end of an infinite sequence would be truly exceptional
"""

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


print(first(["1st", "2nd", "3rd"]))
print(first({"1st", "2nd", "3rd"}))
