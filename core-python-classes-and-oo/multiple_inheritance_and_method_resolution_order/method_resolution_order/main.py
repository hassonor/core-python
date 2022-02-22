from simple_list import *
from diamond import *

print(SortedIntList.__mro__)  # The Method Resolution Order for a class is stored on __mro__
print(D.__mro__)

"""
(<class 'simple_list.SortedIntList'>, <class 'simple_list.IntList'>, <class 'simple_list.SortedList'>, 
<class 'simple_list.SimpleList'>, <class 'object'>)

(<class 'diamond.D'>, <class 'diamond.B'>, <class 'diamond.C'>, <class 'diamond.A'>, <class 'object'>)
"""

d = D()
print(d.func())  # -> Will Print 'B.func'
