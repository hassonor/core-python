import sys

# 8.3. Handling Exceptions
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))  # the exception type
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # unpack args
    print('x =', x)
    print('y =', y)

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)}")
#     raise


# def this_fails():
#     x2 = 1 / 0
#
#
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


def func():
    raise ConnectionError


# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)
divide(2, 0)
divide("2", 1)

# 8.10. Enriching Exceptions with Notes
