"""
This solution is another approach using a recursive function. This recursive
function has a parameter determining if the current node is a left node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_of_left_leaves(self, root: TreeNode) -> int:
        def helper(node, is_left):
            # check if the node is empty
            if not node:
                return 0

            # check if the node is a left leaf node
            if is_left and not node.left and not node.right:
                return node.val + helper(node.right, False)

            return helper(node.left, True) + helper(node.right, False)

        return helper(root, False)
