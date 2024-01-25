def is_palindrome_1(x):
    if x < 0:
        return False

    list_number = list(str(x))

    for index, ele in enumerate(list_number):
        if index > len(list_number) / 2:
            return True
        if list_number[index] != list_number[len(list_number) - index - 1]:
            return False


def is_palindrome_2(x):
    if x < 0:
        return False

    list_num = str(x)
    reversed_list = list_num[::-1]

    return list_num == reversed_list


print(is_palindrome_1(1122113))
print(is_palindrome_2(1122113))

print(is_palindrome_1(1221))
print(is_palindrome_2(1221))
