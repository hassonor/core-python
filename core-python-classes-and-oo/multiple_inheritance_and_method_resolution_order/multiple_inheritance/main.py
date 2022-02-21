from simple_list import *

sil = SortedIntList([40, 22, 2])
print(sil)

sil.add(-1111)
print(sil)

# sil2 = SortedIntList([1, 2, "Or"])   will cause TypeError: because the inheritance from IntList too :)


print(SortedIntList.__base__)  # Will Print <class 'simple_list.IntList'> (Because it is the fist inheritance)
