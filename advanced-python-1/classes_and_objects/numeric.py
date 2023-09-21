# Define a class called Point to represent a point in 2D space
class Point:
    # Initialize a Point object with coordinates x and y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define the string representation of a Point object
    def __repr__(self):
        return "<Point x:{0}, y:{1}>".format(self.x, self.y)

    # Define addition for Point objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Define subtraction for Point objects
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Define in-place addition for Point objects
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # Define multiplication for Point objects (scalar multiplication)
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    # Define true division for Point objects (scalar division)
    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)


# Create two Point objects and display them
p1 = Point(1, 2)
p2 = Point(3, 3)
print(p1, p2)

# Add the two Point objects and display the result
p3 = p1 + p2
print(p3)

# Subtract p1 from p2 and display the result
p4 = p2 - p1
print(p4)

# Update p1 in-place by adding p2
p1 += p2
print(p1)

# Multiply p1 by a scalar (2) and display the result
p5 = p1 * 2
print(p5)

# Divide p2 by a scalar (2) and display the result
p6 = p2 / 2
print(p6)
