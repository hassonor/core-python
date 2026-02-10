"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Approach: Kadane's Algorithm — track current subarray sum, reset when it goes negative.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    assert max_sub_array([-1]) == -1
    print("All tests passed!")
