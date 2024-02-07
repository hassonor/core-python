"""
Arbitrary keyword arguments
-> Prefix argument with ** to accept arbitrary keyword arguments
-> Conventionally called **kwargs
->
"""


# def tag(name, **kwargs):
#     print(name)
#     print(kwargs)
#     print(type(kwargs))

def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result


print(tag('img', src="MyPic.jpg", alt="Cool Pic by Or Hasson", border=1))


def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


print_args(1, 2, 3, 4, 5)

t = (11, 12, 13, 14)
print_args(*t)


def print_args_2(arg1, arg2, *args, kwarg1, kwarg2):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)


print_args_2(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7)


def print_args_3(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


print_args_3(1, 2, 3, 4, 5, kwarg1=7, kwarg2=7, kwarg3=8, kwarg4=9)

"""
Positional-only Arguments -> Python 3.8 or later.
Why Positional-only arguments?
-> Parity with modules implemented in other languages
-> Prevent formal argument names from becoming part of the API
    -> *This prevents dependencies on the name*
    -> *Useful when the names have no semantic meaning*
"""


def number_length(x, /):
    return len(str(x))


print(number_length(2112))

# print(number_length(x=31557600)) -> will raise TypeError: number_length() got some positional-only
# arguments passed as keyword arguments: 'x'
