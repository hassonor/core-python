# Importing the defaultdict class from the collections' module.
from collections import defaultdict

# A sample list containing repeated fruit names.
fruits = ['kiwi', 'pear', 'apple', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']

# Initializing a defaultdict with int type. This means that every new key will have a default value of 0.
fruit_counter = defaultdict(int)

# Iterating over each fruit in the fruits list.
for fruit in fruits:
    # For each fruit, increment its count by 1.
    # If the fruit is not yet in the fruit_counter, it gets automatically added with a default value of 0.
    fruit_counter[fruit] += 1

# Printing the fruit count.
print(fruit_counter)
