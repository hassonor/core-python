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
