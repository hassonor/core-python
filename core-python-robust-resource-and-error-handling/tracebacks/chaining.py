import math
from traceback import print_tb


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        print(e.__traceback__)
        print_tb(e.__traceback__)

    print("Done")


inclination(0, 5)
