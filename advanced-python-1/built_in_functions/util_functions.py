# Initialize a list containing integer elements
list1 = [1, 2, 3, 0, 5, 6, 7]

# The 'any' function returns True if at least one element in the list is True (i.e., not zero or not empty)
# Since list1 contains elements that are not zero, any(list1) will return True
print(any(list1))

# The 'all' function returns True only if all elements in the list are True (i.e., not zero or not empty)
# Since list1 contains a zero, all(list1) will return False
print(all(list1))

# The 'max' function returns the largest element in the list, which is 7 in this case
print(max(list1))

# The 'min' function returns the smallest element in the list, which is 0 in this case
print(min(list1))

# The 'sum' function returns the sum of all elements in the list, which is 24 in this case
print(sum(list1))
