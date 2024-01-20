import math


class Vector:
    """
    A two-dimensional vector class that supports basic vector operations like
    addition, multiplication, absolute value, and boolean representation.
    """

    def __init__(self, x=0, y=0):
        """
        Initialize a Vector instance.

        :param x: The x-coordinate of the vector (defaults to 0).
        :param y: The y-coordinate of the vector (defaults to 0).
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Return the string representation of the Vector instance.
        """
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        """
        Return the magnitude (or length) of the vector.
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        Return False if the vector is at the origin, else True.
        """
        return bool(abs(self))

    def __add__(self, other):
        """
        Add two vectors using the '+' operator.

        :param other: The other Vector instance to add.
        :return: A new Vector instance representing the sum.
        :raises TypeError: If 'other' is not an instance of Vector.
        """
        if not isinstance(other, Vector):
            raise TypeError(f"Unsupported operand type(s) for +: 'Vector' and '{type(other).__name__}'")
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        Multiply the vector by a scalar using the '*' operator.

        :param scalar: The scalar value to multiply by.
        :return: A new Vector instance representing the product.
        :raises TypeError: If 'scalar' is not a numeric type.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Multiplication with non-numeric type '{type(scalar).__name__}'")
        return Vector(self.x * scalar, self.y * scalar)
