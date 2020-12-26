"""
This solution switches every node's left and right child from bottom to right.
At the end the tree will be inverted.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        # if the root is empty, return itself (None)
        if not root:
            return root

        # switch the values
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        # return the root's value
        return root
