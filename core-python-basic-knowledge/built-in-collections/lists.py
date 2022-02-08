# Lists
"""
Negative indices:
Index from the end of sequences using negative numbers
The last element is at index -1.

Slicing:
Extended form of indexing for referring to a portion of a list
or other sequence. Syntax: a_list[start:stop]

"""

s = [3, 186, 4431, 74400, 1048443]
print(s[1:-1])
print(s[2:])
print(s[:2])
print(s[:])

# Shallow Copies
r = s[:]
print(r is s)  # False
print(r == s)  # true (r is a copy of s)

u = s.copy()  # same as u = s[:]
print(u is s)  # False
print(u == s)  # true (u is a copy of s)

"""
list.index()
Find the location of an object in a list.
Returns the index of the first list element which is equal to the argument.
"""

w = "the quick brown fox jumps over the lazy dog".split()
i = w.index('fox')
print(w.count("the"))

"""
del 
Remove an element from a list by index.
Syntax: del a_list[index]
"""

u = "today is a very rainy day but i like the sun".split()
print(u)

del u[3]
print(u)

u.remove('day')
print(u)

del u[u.index('like')]
print(u)

"""
list.insert()
Insert an item into a list.
Accepts an item and the index of the new item.
"""

a = 'I accidentally the whole universe'.split()
print(a)

a.insert(2, 'destroyed')
print(a)

a = ' '.join(a)
print(a)

m = [2, 1, 3]
n = [4, 7, 11]

k = m + n
print(k)
k += [18, 29, 47]
print(k)

k.extend([76, 129, 199])
print(k)

"""
list.reverse() and list.sort()
Common operations that modify a list in place

Key Parameter to list.sort()
-> Can be any callable object that accepts a single parameter.
-> Items passed to callable and sorted on its return value.
"""

g = [1, 11, 21]
print(g)

g.reverse()
print(g)

d = [17, 41, 29]
print(d)

d.sort()
print(d)

d.reverse()
print(d)

h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
print(h)

h.sort(key=len)
print(h)

h = ' '.join(h)
print(h)

"""
Reversing and sorting into copies
----------------------------------
reversed() and sorted() are out-of-place equivalents to list.reverse() and list.sort()
The return a reverse iterator and a new list, respectively
"""

x = [4, 9, 2, 1]
y = sorted(x)
print(y)
print(x)

p = [9, 3, 1, 0]
q = reversed(p)
q = list(q)
print(q)

"""
Summary:
-> List supports indexing from the end with negative indices.
-> Slicing copies all of part of a list.
-> The full slice is a common idiom for copying lists.
-> Use list.index() and list.count() to look for elements in a list.
-> Use the del keyword to remove elements from a list.
-> Sort and reverse lists in-place with list.sort() and list.reverse()
-> sorted() and reversed() sort and reverse any iterable.
-> List copies are shallow, only coping the references.
"""
