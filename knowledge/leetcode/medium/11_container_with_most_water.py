"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an where each represents a point at
coordinate (i, ai). Find two lines that together with the x-axis form a container
that holds the most water.

Approach: Two pointers — start from both ends, move the shorter line inward.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_area(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    print("All tests passed!")
