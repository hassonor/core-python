import collections

Point = collections.namedtuple("Point", "x y")

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1, p2)
print(p1.x, p1.y)

p1 = p1._replace(x=10)
print(p1)
