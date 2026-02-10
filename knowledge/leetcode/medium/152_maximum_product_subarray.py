"""
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product,
and return the product.

Approach: Track both current max and current min at each step,
because a negative number can flip min to max.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_product(nums: List[int]) -> int:
    result = max(nums)
    cur_min = 1
    cur_max = 1

    for num in nums:
        if num == 0:
            cur_min, cur_max = 1, 1
            continue
        tmp = cur_max * num
        cur_max = max(num * cur_max, num * cur_min, num)
        cur_min = min(tmp, num * cur_min, num)
        result = max(result, cur_max)

    return result


if __name__ == "__main__":
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
    assert max_product([-2, 3, -4]) == 24
    assert max_product([0, 2]) == 2
    print("All tests passed!")
