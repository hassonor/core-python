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
            raise ValueError('invalid user response')
        print(reminder)


def triangle_math(e1=20, e2=20, angle=math.pi / 2):
    return e1 * e2 * math.sin(angle) / 2


print(triangle_math(angle=1))
print(triangle_math(angle=3.14159, e2=4, e1=3))
print(triangle_math(e1=3, angle=3.14159, e2=3))


def concat(separator, *args):
    return separator.join(args)


print(concat("/", "06", "01", "2024"))


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
# pos_only_arg(arg=1) will produce and error/warning

# kwd_only_arg(3) will produce and error/warning
kwd_only_arg(arg=3)

# combined_example(1, 2, 3) will produce and error/warning
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


# combined_example(pos_only=1, standard=2, kwd_only=3) will produce and error/warning

def foo(name, /, **kwargs):
    return 'name' in kwargs


def foo2(name, **kwargs):
    return 'name' in kwargs


print(foo(1, **{'name': 2}))
print(foo(1, **{'no_name': 2}))


# print(foo2(1, **{'name': 2}))  Doesn't work


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))  # 42
print(f(1))  # 43

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)

f(1)
