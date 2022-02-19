from base import Sub
from simple_list import SortedList

# demo 1 -> both base and sub init invoked
s = Sub()

# demo 2
sl = SortedList([4, 2, 1, 3, 8, 0])
print(sl)

sl.add(-51)
print(sl)
