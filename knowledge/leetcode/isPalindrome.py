def is_palindrome(num):
    if num < 0:
        return False
    str_1 = str(abs(num))
    str_2 = str_1[::-1]  # save the reverse num
    print(str_2)
    return str_1 == str_2


print(is_palindrome(7107))
