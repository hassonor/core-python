"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal
of its nodes' values (i.e., from left to right, level by level).

Approach: BFS with a queue. Process one level at a time.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result: List[List[int]] = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level: List[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


if __name__ == "__main__":
    # Tree: [3, 9, 20, None, None, 15, 7]
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    assert level_order(TreeNode(1)) == [[1]]
    assert level_order(None) == []
    print("All tests passed!")
