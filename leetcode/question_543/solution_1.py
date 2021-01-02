"""
This solution uses a recursive function to iterate through every node in the
tree and keeps track of the diameter for every node's subtree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        # check if the tree is empty
        if not root:
            return 0

        # set the diameter initially to zero
        diameter = 0

        def helper(node: TreeNode) -> int:
            # if the node is empty, return 0
            if not node:
                return 0

            # get the longest path from the bottom to the current node from the
            # left and right subtree
            left = helper(node.left)
            right = helper(node.right)

            nonlocal diameter
            # We connect the longest path from the left and right subtree.
            # Check if we can get a larger diameter
            diameter = max(left + right, diameter)

            # return the longer path plus 1 (adding the current node)
            return max(left, right) + 1

        helper(root)
        return diameter
