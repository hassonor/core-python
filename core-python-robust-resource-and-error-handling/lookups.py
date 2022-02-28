def lookups():
    s = [1, 3, 5]
    try:
        item = s[4]
    except IndexError:
        print("Handled IndexError")

    d = dict(a=61, b=62, c=64)
    try:
        value = d['x']
    except KeyError:
        print("Handled KeyError")


lookups()