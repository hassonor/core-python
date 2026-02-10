"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Approach: Iterative — track previous, current, and next pointers.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def to_list(head: Optional[ListNode]) -> list[int]:
    """Helper to convert linked list to Python list for testing."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(values: list[int]) -> Optional[ListNode]:
    """Helper to create linked list from Python list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    assert to_list(reverse_list(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(from_list([1, 2]))) == [2, 1]
    assert to_list(reverse_list(from_list([]))) == []
    print("All tests passed!")
