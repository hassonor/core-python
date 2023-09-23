# Import the itertools module
import itertools

# Initialize a list of names
seq1 = ["Joe", "Or", "Hasson", "John", "Mike"]

# Create an iterator that returns elements from the iterable (seq1), and saves a copy of the iterable to cycle through again.
cycle1 = itertools.cycle(seq1)

# Display the next three elements in the cycle
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))

# Create an iterator that returns evenly spaced values starting with 100 and with steps of 10
count1 = itertools.count(100, 10)

# Display the next three elements from the count iterator
print(next(count1))
print(next(count1))
print(next(count1))

# Create an iterator that returns accumulated sums of the values in the list 'vals'
vals = [10, 20, 30, 40, 50, 40, 30]
acc = itertools.accumulate(vals)

# Display the accumulated sums
print(list(acc))

# Create an iterator that returns the running maximum values from the list 'vals'
running_max_values = itertools.accumulate(vals, max)

# Display the running maximum values
print(list(running_max_values))

# Create an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next
# iterable
chain_strings = itertools.chain("ABCD", "1234")

# Display the chained iterable
print(list(chain_strings))

# Create an iterator that drops elements as long as the test_function is True; thereafter, returns every element
print(list(itertools.dropwhile(lambda x: x < 40, vals)))

# Create an iterator that returns elements as long as the test_function is True
print(list(itertools.takewhile(lambda x: x < 40, vals)))
