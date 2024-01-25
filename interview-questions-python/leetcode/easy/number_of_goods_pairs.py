def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pairs = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                pairs.append((j, i))
                print((i, j))


numIdenticalPairs([1, 2, 3, 1, 1, 3])
