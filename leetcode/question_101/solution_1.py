"""
This solution uses a recursive function to complete the question.
It compares each symmetric node's equality
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        # if the tree is empty, return true
        if root is None:
            return True

        # check if each node is symmetric
        return self.check_nodes(root.left, root.right)

    def check_nodes(self, left, right):
        # if the left and right node are empty, return true
        # if only one of them is empty, return false
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            # check the nodes' equality and check their subtree's equality
            return (
                left.val == right.val
                and self.check_nodes(left.left, right.right)
                and self.check_nodes(left.right, right.left)
            )
