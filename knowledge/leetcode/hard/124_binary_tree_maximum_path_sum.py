"""
124. Binary Tree Maximum Path Sum

Given the root of a binary tree, return the maximum path sum of any non-empty path.
A path can start and end at any node in the tree.

Approach: DFS — at each node, compute the max gain from left and right subtrees.
Update global max considering the path through the current node.

Time Complexity: O(n)
Space Complexity: O(h) where h is tree height
"""

from typing import Optional


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


def max_path_sum(root: Optional[TreeNode]) -> int:
    max_sum = float("-inf")

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0

        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        # Path through this node as the highest point
        path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, path_sum)

        # Return max gain this node can contribute to its parent
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum


if __name__ == "__main__":
    # Tree: [1, 2, 3]
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert max_path_sum(root1) == 6

    # Tree: [-10, 9, 20, None, None, 15, 7]
    root2 = TreeNode(
        -10,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )
    assert max_path_sum(root2) == 42

    # Single negative node
    assert max_path_sum(TreeNode(-3)) == -3

    print("All tests passed!")
