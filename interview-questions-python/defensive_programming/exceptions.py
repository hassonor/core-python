import sys

# Example 1
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")

# Example 2
try:
    f = open("example.txt")
    s = f.readline()
    i = int(s.strip())
    f.close()
except OSError as err:
    print(f"OS error:{err}")
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print("all ok")


# Example 3
def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print("Handling run-time error:", err)

# Example 4
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly

    x, y = inst.args  # unpack args
    print('x = ', x)
    print('y = ', y)
