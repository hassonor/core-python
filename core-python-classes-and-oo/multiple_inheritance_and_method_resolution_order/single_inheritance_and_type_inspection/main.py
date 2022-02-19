from base import Sub
from simple_list import *

# demo 1 -> both base and sub init invoked
s = Sub()

# demo 2
sl = SortedList([4, 2, 1, 3, 8, 0])
print(sl)

sl.add(-51)
print(sl)

# demo 3 -> isinstance method
sl2 = SortedList([3, 2, 1])
print(isinstance(sl2, SortedList))
print(isinstance(sl2, SimpleList))

# demo 4 -> IntList

il = IntList([11, 22, 33, 44])
il.add(35)
print(il)

# print(il.add("Hey"))  # will raise Error.

# demo 5 -> example of issubclass()
print(issubclass(IntList, SimpleList))  # -> True
print(issubclass(SortedList, SimpleList))  # -> True
print(issubclass(SortedList, IntList))  # -> False
