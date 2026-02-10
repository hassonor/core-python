"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

Approach: Floyd's Tortoise and Hare — slow pointer moves 1 step, fast moves 2.
If they meet, there's a cycle.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


if __name__ == "__main__":
    # Test 1: Cycle exists (3 -> 2 -> 0 -> -4 -> back to 2)
    node4 = ListNode(-4)
    node3 = ListNode(0, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(3, node2)
    node4.next = node2
    assert has_cycle(node1) is True

    # Test 2: No cycle
    a = ListNode(1, ListNode(2, ListNode(3)))
    assert has_cycle(a) is False

    # Test 3: Empty list
    assert has_cycle(None) is False

    print("All tests passed!")
