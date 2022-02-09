def hyper_volume_1(*args):
    print(args)
    print(type(args))


def hyper_volume_2(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v


def hyper_volume_3(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


hyper_volume_1(3, 4)
hyper_volume_1(3, 4, 5)

print(hyper_volume_2(2, 4))
print(hyper_volume_2(2, 4, 6))
print(hyper_volume_2(2, 4, 6, 8))

# hyper_volume_len() # will raise StopIteration Exception

"""
Translate the Exception
-> Catch the StopIteration exception thrown by next()
-> Translate it into the more predictable TypeError
"""

print(hyper_volume_3(2, 4))
print(hyper_volume_3(2, 4, 6))
print(hyper_volume_3(2, 4, 6, 8))

print(hyper_volume_3())  # will raise TypeError: hyper_volume_3() missing 1 required positional argument: 'length'
