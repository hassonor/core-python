def two_sum(nums, target):
    for index1, ele1 in enumerate(nums):
        for index2, ele2 in enumerate(nums):
            if index1 != index2 and (ele1 + ele2 == target):
                return [index1, index2]
