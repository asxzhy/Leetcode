"""
This solution uses a recursive function to complete the problem.
It walks through the binary tree and get the larger depth
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        # checks if the node is empty, if so return 0
        if root is None:
            return 0

        # get the max depth from the left and right subtree.
        # add 1 for the current depth
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
