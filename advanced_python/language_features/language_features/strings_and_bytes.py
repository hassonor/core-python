b = bytes([0x41, 0x42, 0x43, 0x44])
print(b)

s = "This is a string"
print(s)

# print(s+b) -> Error

# Decode the bytes
s2 = b.decode('utf-8')
print(s + s2)

# Encode the string to utf-8
b2 = s.encode("utf-8")
print(b + b2)

# Encode the string to utf-32
b3 = s.encode("utf-32")
print(b3)
