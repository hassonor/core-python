from simple_list import *
from animals import *

print(SortedIntList())  # -> <super: <class 'IntList'>, <SortedIntList object>>

print(SortedIntList.__mro__)

print(Animal.description())  # -> 'An Animal'
print(Bird.description())  # -> 'An animal with wings'
print(Flamingo.description())  # -> 'An animal with wings and fabulous ping feathers'
