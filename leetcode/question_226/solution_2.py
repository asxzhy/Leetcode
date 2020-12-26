"""
This solution is similar to solution 1 but this one is faster than the first
solution.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        # if the root is empty, return itself (None)
        if root:
            # switch the node's left and right child
            root.left, root.right = root.right, root.left

            # go to the left and right child and switch their children
            self.invertTree(root.right)
            self.invertTree(root.left)

        # return the root's value
        return root
