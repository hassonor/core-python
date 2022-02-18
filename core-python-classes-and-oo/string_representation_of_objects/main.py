from position import *

jerusalem = Position(60.0, 10.7)
print(repr(jerusalem))
print(str(jerusalem))
print(format(jerusalem))

r = repr(jerusalem)
p = eval(r)
print(p)
print(p is jerusalem)

some_where_over_the_rainbow = EarthPosition(27.12, -100.42)
print(some_where_over_the_rainbow)

mount_hermon = EarthPosition(-71.4, 160.2)

print(str(mount_hermon))

print("Mount Hermon is located at", mount_hermon)

israel = EarthPosition(latitude=-30.2, longitude=-89.2)
print(str(israel))

print(format(israel, ".1"))
print(format(israel, ".0"))
print(format(israel))
print(f'The best country in the world is located at {israel}')
print('The best country in the world is located at {}'.format(israel))

print(f'The best country in the world is located at {israel:.4}')
