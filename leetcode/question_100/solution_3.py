"""
This solution directly compares every nodes in the two trees.
"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        # if both node is null return true
        if p is None and q is None:
            return True

        # if the nodes are different, return false
        if p is None or q is None or p.val != q.val:
            return False

        # check the next nodes' equality
        return self.is_same_tree(p.left, q.left) and \
               self.is_same_tree(p.right, q.right)
