"""
This solution uses the max_depth function as a helper function to get
each node's subtree's depth and subtract the depth to see if the difference
is greater and 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        # check if the node is empty
        if not root:
            return True

        # the current node is balanced when its left and right subtree's depth
        # is not greater than one, and then proceed to its children to check
        # if they are balanced
        return (
            abs(
                self.max_depth(root.left) - self.max_depth(root.right),
            )
            <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def max_depth(self, node):
        # check if the node is empty
        if not node:
            return 0

        # find the max depth between the left and right subtree and then add 1
        return (
            max(
                self.max_depth(node.left),
                self.max_depth(node.right),
            )
            + 1
        )
