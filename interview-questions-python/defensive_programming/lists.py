"""
Lists:
______
- Lists are editable and mutable
- Common Methods:
    - append() - add an element at the end of the list
    - clear() - clear all elements from a list
    - copy() - return a copy of the list
    - count() - count how many times the value appears in the list
    - extend() - join a series of additional elements to the list
    - insert(index,value) - add an element (value) to the index place in the list
    - sort() - sort the list
    - reverse() - reverse the order of the list
"""
list1 = [1, 2, 5]
print(list1)

list2 = ["apple", "banana", "lemon"]
print(list2)

list1 = list1 + list2
print(list1)

# Create empty list via constructor
my_list = list()
print(my_list)

squares = [1, 4, 9, 16, 25, 36]
print(len(squares))
print(squares[0:2])
print(squares[-2:-1])
print(squares[-2:])

# Splitting string to list and back to string

abc = "this is a sentence of stupid words"
list_abc = abc.split(" ")
print(list_abc)
print("_".join(list_abc))

# Aliasing example
fruit = ["banana", "apple", "cherry"]
print(fruit)
vegs = fruit
fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)
print(vegs)

# Loops of list
mylist = ["tHIS", "iS", "a", "lisT", "of", "words"]
for word in mylist:
    # print(word.capitalize())  # Capital the first letter and UnCapital all the rest of the word
    # If we don't want a new line each print
    print(word.capitalize(), end=' ')

# Access to strings as chars
a = "Encyclopedia"
print(a[4])
print(a[-2:])
print(a[0:3])
for c in a:
    print(c.upper(), end="_")

# More lists types
a, b = 0, 1
for num in range(7):  # all numbers from 0 to 6 (0 to N-1)
    print(a)
    a, b = b, a + b
