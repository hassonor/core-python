def add_binary(a, b):
    c = str(bin(int(a, 2) + int(b, 2)))
    return c[2:]
