def move_zeros(arr):
    new_sorted_arr = []
    new_zero_arr = []

    for val in arr:
        if val == 0 and type(val) != bool:
            new_zero_arr.append(val)
        else:
            new_sorted_arr.append(val)

    return new_sorted_arr + new_zero_arr


print(type(False))
print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
