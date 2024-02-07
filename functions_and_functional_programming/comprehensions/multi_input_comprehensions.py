print(list((x, y) for x in range(5) for y in range(5)))

# Same
points = []
for x in range(5):
    for y in range(5):
        points.append((x, y))

print(points)