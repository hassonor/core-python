import json
import math

# 7.1.1: Formatted String Literals
print(f'The value of pi is approximately {math.pi: .3f}')

table = {'Sjoed': 4127, 'Or': 4097, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

"""
Other modifiers can be used to convert the value before it is formatted. 
'!a' applies ascii(), 
'!s' applies str(), 
and '!r' applies repr():
"""
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

"""
The = specifier can be used to expand an expression to the text of the expression, 
an equal sign, then the representation of the evaluated expression:
"""
bugs = 'roaches'
count = 17
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

# 7.1.2: The String format() method
print("We are the {} who say '{}!'".format('knights', 'Ni'))
print("{0} and {1}".format('spam', 'eggs'))
print("{1} and {0}".format('spam', 'eggs'))
print("This {food} is {adjective}.".format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Or', 'Hasson',
                                                   other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

"""
There is another method, str.zfill(), which pads a numeric string on the left with zeros. 
It understands about plus and minus signs:
"""
print('12'.zfill(5))  # '00012'
print('-3.14'.zfill(7))  # '-003.14'
print('3.14159265359'.zfill(5))  # '3.14159265359'

f = open('workfile', 'wb+')
f.write(b'0123456789abcdef')

f.seek(5)  # Go to the 6th byte in the file

print(f.read(1))

f.seek(-3, 2)  # Go to the 3rd byte before the end

print(f.read(1))

# 7.2.2: Saving structured data with json
x = [1, 'simple', 'list']
json.dumps(x)
