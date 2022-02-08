def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


print(add_spam())
print(add_spam())

# Protocols
"""
Protocols:
-> A set of operations that a type must support to implement the protocol.
-> Do not need to be defined as interfaces or base classes.
-> Types only need to provide functioning implementations.

Protocol | Implementing collections
--------- -------------------------
Container -> str, list, dict, range, tuple, set, bytes | item in container , item not in container
Sized -> str, list, dict, range, tuple, set, bytes | len(container)
Iterable -> str, list, dict, range, tuple, set, bytes | Yield items one by one as they are requested. 
                                                        for item in iterable:
                                                           print(item)
Sequence -> str, list, range, tuple, bytes | item = sequence[index] 
                                             i = sequence.index(item)
                                             num = sequence.count(item)
                                             r = reversed(sequence)
                                             iterable, sized, and container
Mutable Sequence -> list 
Mutable Set -> set
Mutable Mapping -> dict
"""
