print({x * y for x in range(10) for y in range(10)})

g = ((x, y) for x in range(10) for y in range(x))
print(list(g))
