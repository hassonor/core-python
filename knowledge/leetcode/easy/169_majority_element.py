"""
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than n/2 times.

Approach: Boyer-Moore Voting Algorithm.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def majority_element(nums: List[int]) -> int:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


if __name__ == "__main__":
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element([1]) == 1
    print("All tests passed!")
