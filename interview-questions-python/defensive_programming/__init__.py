class Point:
    def __init__(self, x_color, y_color):
        self.x = x_color
        self.y = y_color

    def move(self, add_x, add_y):
        self.x += add_x
        self.y += add_y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def reset(self, x_cor=0, y_cor=0):
        self.x = x_cor
        self.y = y_cor


if __name__ == "__main__":
    p = Point(1, 2)
    print(Point.__dict__)
    print(p.__dict__)
    print(p)
    p.__setattr__("reset", p.__getattribute__("move"))
    p.reset(4, 4)
    print(p)

    p.myvar = "trial text"
    print(dir(p))
    print(globals())
