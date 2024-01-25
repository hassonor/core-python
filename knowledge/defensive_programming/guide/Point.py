class Point:
    def __init__(self, x_cor, y_cor):
        self.x = x_cor
        self.y = y_cor

    def move(self, add_x, add_y):
        self.x += add_x
        self.y += add_y

    def __str__(self):
        return f"({self.x},{self.y})"

    def reset(self, x_cor=0, y_cor=0):
        self.x = x_cor
        self.y = y_cor


p = Point(11, 22)
p.move(9, 5)
print(p)
print(dir(Point))
print(dir(p))
# p.__setattr__("reset", p.__getattribute__("move"))

p.reset()
print(p)
p.reset(10, 10)
print(p)
p.reset(30)
print(p)
p.reset(y_cor=30)
print(p)
