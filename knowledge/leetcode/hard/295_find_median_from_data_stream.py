"""
295. Find Median from Data Stream

Design a data structure that supports adding integers and finding the median.

Approach: Two heaps — a max-heap for the lower half, a min-heap for the upper half.
Keep them balanced so the median is always accessible in O(1).

Time Complexity: O(log n) per addNum, O(1) per findMedian
Space Complexity: O(n)
"""

import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.small: list[int] = []  # Max-heap (inverted values)
        self.large: list[int] = []  # Min-heap

    def add_num(self, num: int) -> None:
        # Push to max-heap (invert for max-heap behavior)
        heapq.heappush(self.small, -num)

        # Ensure max of small <= min of large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes (small can have at most 1 more than large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0

    mf2 = MedianFinder()
    mf2.add_num(6)
    assert mf2.find_median() == 6.0
    mf2.add_num(10)
    assert mf2.find_median() == 8.0
    mf2.add_num(2)
    assert mf2.find_median() == 6.0

    print("All tests passed!")
