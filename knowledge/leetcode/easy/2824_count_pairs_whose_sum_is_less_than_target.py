def count_pairs(nums, target):
    pairs_count = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                pairs_count += 1

    return pairs_count
