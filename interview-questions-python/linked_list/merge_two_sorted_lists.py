# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy node and a current pointer to traverse the merged list
    dummy = ListNode(0)
    current = dummy

    # While there are nodes in both lists
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        # Move the current pointer to the next position in the merged list
        current = current.next

    # If nodes are left in list1, append them
    if list1 is not None:
        current.next = list1
    # If nodes are left in list2, append them
    elif list2 is not None:
        current.next = list2

    # Return the merged list starting from the next of the dummy node
    return dummy.next

# Memory Details: 16.16MB - Beats 96.40% of users with Python3
# Runtime Details: 48ms - Beats 29.04% of users with Python3

# Complexity Analysis:
# Time Complexity: O(n + m), where n and m are the lengths of list1 and list2, respectively.
# We traverse each list at most once.
# Space Complexity: O(1) - We only use a constant amount of space for the dummy node and a few variables.
