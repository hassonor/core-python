"""
23. Merge k Sorted Lists

You are given an array of k linked-lists, each sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Approach: Min-heap (priority queue) — push all heads, pop smallest, push its next.

Time Complexity: O(N log k) where N is total nodes and k is number of lists
Space Complexity: O(k)
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap: list[tuple[int, int, ListNode]] = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next


def from_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    lists = [from_list([1, 4, 5]), from_list([1, 3, 4]), from_list([2, 6])]
    assert to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]

    assert to_list(merge_k_lists([])) == []
    assert to_list(merge_k_lists([None])) == []

    print("All tests passed!")
