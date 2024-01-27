# Build a list of unicode points from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(symbol)
print(codes)  # ['$', '¢', '£', '¥', '€', '¤']

# Build a list of unicode points from a string, using a listcomp
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)  # [36, 162, 163, 165, 8364, 164]

# The same list built by a listcomp and map/filter composition
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)  # [162, 163, 165, 8364, 164]

# With filter,lambda and map
symbols = '$¢£¥€¤'
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)  # [162, 163, 165, 8364, 164]

# Cartesian product using a list comprehension
colors = ['red', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in
           sizes]  # Generate a list of tuples (color,size) elements and order by color
print(tshirts)  # [('red', 'S'), ('red', 'M'), ('red', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

tshirts = [(color, size) for size in sizes for color in
           colors]  # Generate a list of tuples (color,size) elements and order by size

print(tshirts)  # [('red', 'S'), ('white', 'S'), ('red', 'M'), ('white', 'M'), ('red', 'L'), ('white', 'L')]

for color in colors:
    for size in sizes:
        print((color, size))
