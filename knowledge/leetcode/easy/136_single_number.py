"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with O(n) time and O(1) extra space.

Approach: XOR — a ^ a = 0, a ^ 0 = a. XOR all elements; duplicates cancel out.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
    print("All tests passed!")
