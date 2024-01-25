def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    string_x = str(x)
    string_x_reverse = string_x[::-1]

    return string_x == string_x_reverse
