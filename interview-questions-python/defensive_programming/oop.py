import types
import builtins
import marshal

# Create functions at runtime

# Example 1: Creating and executing a function at runtime using compile
f = compile('a=47; print(a)', '', 'exec')
d = types.FunctionType(f, {'__builtins__': builtins})
d()  # This will print 47

# Example 2: Dynamically creating a function from byte-compiled code
# First, compile some code and serialize it using marshal
example_code = compile('print("Hello, world!")', '', 'exec')
serialized_code = marshal.dumps(example_code)

# Now deserialize and create a function from the serialized code
code = marshal.loads(serialized_code)
func = types.FunctionType(code, globals(), 'func')
func()  # This will print "Hello, world!"


class Person:
    i = 12345

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Point:
    def __init__(self, x_color, y_color):
        self.x = x_color
        self.y = y_color

    def move(self, add_x, add_y):
        self.x += add_x
        self.y += add_y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Colpoint(Point):
    def __init__(self, x_color, y_color, color):
        super().__init__(x_color, y_color)
        self.color = color


if __name__ == '__main__':
    p1 = Person("John", 32)
    print(p1.name)
    print(p1.age)
    print(p1.i)

    p = Point(1, 2)
    p.move(10, 21)
    print(p)  # Invoke the __str__ method in Point class

    y = Colpoint(3, 4, "red")
    print(y)

    p.__setattr__("reset", p.__getattribute__("move"))
    p.reset(2, 2)
    print(p)

    cls = type("ExampleClass", (), {'value': 110, 'title': 'This is an example'})
    cls2 = type("ExampleClass", (Point,), {'value': 110, 'title': 'This is another example'})
