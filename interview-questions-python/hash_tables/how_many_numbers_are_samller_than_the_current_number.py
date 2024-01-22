def smallerNumbersThanCurrent(nums):
    output = []
    counter = 0
    for index1, val1 in enumerate(nums):
        for index2, val2 in enumerate(nums):
            if index1 != index2 and val1 > val2:
                counter += 1
        output.append(counter)
        counter = 0

    return output


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
