"""
This solution uses a recursive approach to solve the problem. It creates the
new tree as it goes through both tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # if both tree do not exist, return null
        if not t1 and not t2:
            return None

        # if only t2 exist, return t2
        if not t1:
            return t2

        # if only t1 exist, return t1
        if not t2:
            return t1

        # return a new node with the sum of the two nodes' value and the merged
        # left and right children
        return TreeNode(
            t1.val + t2.val,
            self.merge_trees(t1.left, t2.left),
            self.merge_trees(t1.right, t2.right),
        )
