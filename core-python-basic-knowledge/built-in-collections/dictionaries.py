# Dictionaries
"""
Dictionary internals
Keys -> Must be immutable
Values -> May be mutable

As with lists, dictionary copying is shallow (by default)
"""

names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 50)]

d = dict(names_and_ages)
print(d)

phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo', f='foxtrot')
print(phonetic)

d = dict(goldenrod=0xDaa520, indigo=0x4B0082, seashell=0xFFF5EE)
e = d.copy()
print(e)

f = dict(e)
print(f)

"""
dict.update()
Adds entries from one dictionary into another.
Call this on the dictionary that is to be updated.
"""

g = dict(whear=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)
f.update(g)
print(f)

stocks = {'GOOG': 900, 'AAPL': 420, 'IBM': 204}
stocks.update({'GOOG': 920, 'YHOO': 34})
print(stocks)

"""
Dictionary iteration
--------------------
Dictionaries yield the next key on each iteration.
Values can be retrieved using the square-bracket operator.
"""

for key in stocks:
    print(f"{key} => {stocks[key]}")

for value in stocks.values():
    print(value)

for key in stocks.keys():
    print(key)

"""
dict.items()
Iterates over keys and values in tandem.
Yields a  (key, value) tuple on each iteration.
"""

for key, value in stocks.items():
    print(f"{key} => {value}")

z = {'H': 1, 'Tc': 43, 'Xe': 44}
print(z)

del z['H']
print(z)

m = {'H': [1, 2, 3], 'Tc': [43, 33, 23], 'Xe': [44]}
print(m)

m['H'] += [4, 5, 6, 7]
print(m)

from pprint import pprint as pp

pp(m)

"""
Summary:
-> Dictionaries map from keys to values.
-> Iteration and membership in dictionaries are over keys.
-> Do not assume any order when iterating dictionary keys.
-> dict.keys(), dict.values(), and dict.items() are iterable views into dictionaries.
-> Copy dictionaries with dict.copy() or the dict constructor.
-> Use dict.update() extend one dictionary with another.
"""
