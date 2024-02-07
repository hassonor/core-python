import sys
from math import sqrt


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed.")

    except ValueError as e:
        print(e, file=sys.stderr)

    print("Program execution continues normally here.")

    if __name__ == '__main__':
        main()
