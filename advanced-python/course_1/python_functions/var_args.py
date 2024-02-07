def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(addition(7, 10, 16, 22))
print(addition(1, 2, 3, 4))

nums = [5, 10, 15, 20, 25]
print(addition(*nums))
