"""
This solution uses a recursive function to get the sum of all the left leaf
nodes.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_of_left_leaves(self, root: TreeNode) -> int:
        # check if the tree is empty
        if not root:
            return 0

        # if the node's left child is a leaf node, add its value and check the
        # right subtree
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sum_of_left_leaves(root.right)

        return self.sum_of_left_leaves(root.left) + self.sum_of_left_leaves(root.right)
