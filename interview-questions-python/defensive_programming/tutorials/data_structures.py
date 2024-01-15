import math
from collections import deque

# 5.1: More on Lists
fruit = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruit.count('apple'))
print(fruit.index('banana'))
print(fruit.index('banana', 4))  # Fine the next 'banana' starting at position 4

fruit.reverse()
print(fruit)

fruit.append('grape')
print(fruit)

fruit.sort()
print(fruit)

print(fruit.pop())
print(fruit.pop())
print(fruit)

# 5.1.1: Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print("\n" + str(stack))

print(stack.pop())
print(stack)

# 5.1.2: Using Lists as Queues
queue = deque(["Or", "Ran", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue.popleft())  # The first to arrive is now leaves ("Or")
print(queue.popleft())  # The second to arrive is now leaves ("Ran")
print(queue)

# 5.1.3: List Comprehensions
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
squares.clear()  # clear the list
print(squares)

# Second way
squares = list(map(lambda ele: ele ** 2, range(10)))
print(squares)
squares.clear()  # clear the list
print(squares)

# Third way
squares = [ele ** 2 for ele in range(10)]
print(squares)

cool_tuples_list = [(x, y) for x in [1, 2, 3] for y in [3, 2, 7] if x != y]
print(cool_tuples_list)

vec = [-4, 2, 0, 2, 4, 3, 1]
print([v * 2 for v in vec])
print([v for v in vec if v <= 0])
print([abs(v) for v in vec])

fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([fr.strip() for fr in fresh_fruit])

# Create a list 2-tuples like (number,square)
print([(n, n ** 2) for n in range(10)])

vec2 = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
# Flatten a list using a list comp  with two 'for'
print([num for ele in vec2 for num in ele])

# 5.1.4. Nested List Comprehensions
matrix = [[1, 2, 3, 4], [4, 5, 6, 11], [7, 8, 9, 22]]
print([[row[i] for row in matrix] for i in range(4)])  # transpose the matrix
# equivalent to this
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# equivalent to this
transposed.clear()
print(transposed)
for i in range(4):
    # the following 3 lines implement the nested list comp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# built-in zip
print(list(zip(*matrix)))
# Notice it created a list of tuples unlike the previous examples
# that produced a list of lists like the matrix
# to solve it we can
z_matrix = zip(*matrix)
transposed_z_matrix = [list(row) for row in z_matrix]
print(transposed_z_matrix)

# 5.4: Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # letters in 'a' but not in 'b'
print(a | b)  # letters in 'a' or 'b' or both
print(a & b)  # letters both in 'a' and 'b'
print(a ^ b)  # letter in 'a' or 'b' but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 5.5 Dictionaries
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# Print: {'sape': 4139, 'guido': 4127, 'jack': 4098}

print({x: x ** 2 for x in (2, 4, 6)})
# Print: {2: 4, 4: 16, 6: 36}

print(dict(sape=4139, guido=4127, jack=4098))  # Possible when all keys are strings
# Print: {'sape': 4139, 'guido': 4127, 'jack': 4098}

# 5.6: Looping Techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(f"{k}: {v}")

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(f"{i} {v}")

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f"What is the {q}? It is {a}.")

for i in reversed(range(1, 10, 2)):
    print(i)

basked = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basked):
    print(i)

print('**********')
for i in sorted(set(basked)):
    print(i)

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
