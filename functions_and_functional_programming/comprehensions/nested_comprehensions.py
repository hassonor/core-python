# Nested Comprehensions

vals = [[y * 3 for y in range(x)] for x in range(10)]
print(vals)

# Same
outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)

print(outer)
