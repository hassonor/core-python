values = [x / (x - y) for x in range(100) if x > 50 for y in range(100) if x - y != 0]
print(values)

# Same
values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x - y != 0:
                values.append(x / (x - y))

print(values)

print([(x, y) for x in range(10) for y in range(x)])

# Same
result = []
for x in range(10):
    for y in range(x):
        result.append((x, y))

print(result)
