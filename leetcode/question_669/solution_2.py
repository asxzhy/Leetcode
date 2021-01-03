"""
This solution is similar to the first solution  but changed the if statements
to make it easier to understand
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val < low:
            return self.trim_bst(root.right, low, high)
        if root.val > high:
            return self.trim_bst(root.left, low, high)

        root.left = self.trim_bst(root.left, low, high)
        root.right = self.trim_bst(root.right, low, high)
        return root
