from dataclasses import dataclass


# 9.2.1: Scopes and Namespaces Example

def score_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


score_test()
print("In global scope:", spam)


def outer_function():
    var = "original value in outer_function"

    def middle_function():
        def inner_function():
            nonlocal var  # Refers to 'var' in outer_function (accessible through middle_function)
            var = "modified in inner_function"

        inner_function()
        print("After inner_function:", var)  # Will show the modified value

    middle_function()
    print("After middle_function:", var)  # Will also show the modified value


outer_function()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)

# 9.3.3: Instance Objects
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


# print(x.counter) Will produce an error

# 9.3.5: Class and Instance Variables

class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Pistuk')
e = Dog('Lily')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.kind)  # shared by all dogs

print(d.name)  # unique to d
print(d.tricks)  # unique to d

print(e.name)  # unique to e
print(e.tricks)  # unique to d


# 9.4: Random Remarks
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


# 9.5: Inheritance
"""
Python has two built-in functions that work with inheritance:

Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only 
if obj.__class__ is int or some class derived from int.

Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool 
is a subclass of int. 
However, issubclass(float, int) is False since float is not a subclass of int.
"""


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# 9.7: Odds and Ends
@dataclass
class Employee:
    name: str
    dept: str
    salary: int


orh = Employee('Or', 'Computer Science', 30000)
print(orh.dept)

# 9.8: Iterators
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in "123":
    print(char)
for line in open("../05/data_structures.py"):
    print(line, end='')

s = 'abc'
it = iter(s)
print(it)

print(next(it))  # 'a'
print(next(it))  # 'b'
print(next(it))  # 'c'


# print(next(it)) # raise Traceback: StopIteration


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)

print("**********")

# 9.9: Generators
"""
Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).
 An example shows that generators can be trivially easy to create:
"""


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('orhasson'):
    print(char)

# 9.10: Generator Expressions

print(sum(i * i for i in range(10)))  # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x * y for x, y in zip(xvec, yvec)))  # 70 + 100 + 90 =  260

# unique_words = set(word for line in page for word in line.split())
# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
print(list(data[i] for i in range(len(data) - 1, -1, -1)))
