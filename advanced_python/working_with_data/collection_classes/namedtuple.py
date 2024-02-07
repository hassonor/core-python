# Importing the `collections` module which provides utility functions/classes to work with Python collections
import collections

# Using the `namedtuple` function to create a custom tuple class named "Point".
# This custom tuple will have named fields "x" and "y".
Point = collections.namedtuple("Point", "x y")

# Creating instances of our custom tuple "Point"
p1 = Point(10, 20)
p2 = Point(30, 40)

# Printing the values of our points
print(p1, p2)

# Accessing the individual fields of the namedtuples using dot notation
print(p1.x, p1.y)  # This will print the x and y values of flask_project1
print(p2.x, p2.y)  # This will print the x and y values of p2

# Using the `_replace()` method of namedtuples to create a new Point with modified field values.
# Here, we're updating the x value of flask_project1.
p1 = p1._replace(x=100)

# Printing the updated flask_project1 value
print(p1)
