import math


def average(x, y):
    if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float):
        return (x + 2) / 2
    else:
        print("Wrong variable type")
        return None


print(average(4, 6))


def checks_vars():
    global x  # If we want to update global variable inside a function
    x = 4
    print("Inside x = ", x, " and y = ", y)
    return


x, y = 5, 10
checks_vars()
print("Outside x = ", x, " and y = ", y)


def factorial(n):
    if type(n) is not int:
        print("Invalid argument type.")
        return None
    if n > 0:
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    else:
        print("Invalid negative argument")
        return None


print("Factorial of 7 is: ", factorial(7))
print("Factorial of 7 is: ", math.factorial(7))


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            print('invalid user response')
        print(reminder)


def triangle_math(e1=20, e2=20, angle=math.pi / 2):
    return e1 * e2 * math.sin(angle) / 2


print(triangle_math(angle=1))
print(triangle_math(angle=3.14159, e2=4, e1=3))
print(triangle_math(e1=3, angle=3.14159, e2=3))


def concat(separator, *args):
    return separator.join(args)


print(concat("/", "06", "01", "2024"))
