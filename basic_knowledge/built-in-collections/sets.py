# Sets
"""
Set
-> Unordered collection of unique elements.
-> Sets are mutable.
-> Elements in a set must be immutable.
"""
p = {6, 28, 496, 8128, 12312}
print(p)

print(type(p))

d = {}
print(type(d))  # will be a dict

e = set()
print(type(e))  # will be a set

s = set([2, 4, 16, 64, 4096, 65536, 262144])
print(s)

t = [1, 4, 2, 1, 7, 9, 9]
t = set(t)
print(t)

k = {81, 108}
print(k)

k.add(12)
print(k)

k.add(108)  # no effect already exist.
print(k)

k.update([37, 128, 97])  # adding to the set
print(k)

k.remove(97)
print(k)

# k.remove(97) -> will cause error (97 already removed).

k.discard(97)  # safer method remove an element from a set.
print(k)

j = k.copy()  # Shallow copy
print(j)

m = set(j)
print(m)

"""
Set Algebra:
-> union
-> difference
-> intersection
-> subset
-> superset
-> disjoint
"""

blue_eyes = {'Olivia', 'Harry', 'Lilly', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lilly', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

print(blue_eyes.union(blond_hair))  # all people with blue eyes / blond hair or both.
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))

print(blue_eyes.intersection(blond_hair))  # all people with blue eyes and blond hair.
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))

print(blond_hair.difference(blue_eyes))  # all people with blond hair that don't have blue eyes.
print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))

print(blond_hair.symmetric_difference(blue_eyes))  # all people with blue eyes  or blond hair (not both).
print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))

print(smell_hcn.issubset(blond_hair))  # all the people whom smell hydrogen cyanide also have blond hair.

print(
    taste_ptc.issuperset(smell_hcn))  # all the people whom  taste Phenylthiocarbamide  can also taste hydrogen cyanide.

print(a_blood.isdisjoint(o_blood))  # taste 2 sets not have members in common

"""
Summary:
-> Sets are unordered collection of unique elements.
-> Sets support powerful set-algebra operations and predicates
-> Built-in collection can be organized by protocols.
-> Underscore often represents unused values.
-> The pprint module support pretty printing of compound data structures.
"""
