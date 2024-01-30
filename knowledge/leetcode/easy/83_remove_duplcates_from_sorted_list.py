class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode):
    if head is None:
        return []

    seen_values = set()

    current_node = head
    seen_values.add(current_node.val)

    while current_node.next is not None:
        if current_node.next.val in seen_values:
            current_node.next = current_node.next.next
        else:
            seen_values.add(current_node.next.val)
            current_node = current_node.next

    return head
