"""
This solution compares the left and right subtree of the input tree.
It gets all the node values from the left subtree using pre-order traversal
and gets all the node values from the right subtree symmetrically, (access the
left and right node in reversed order) then compares them.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        # check if it is an empty tree
        if root is None:
            return True

        # if the left subtree is equal to the right subtree reversed, then the
        # binary tree is symmetric
        return self.helper_left(root.left) == self.helper_right(root.right)

    def helper_left(self, node):
        # if the node is empty, add a null to the return list
        if node is None:
            return [None]

        # add the node's value and proceed to the left node and then right node
        return [node.val] + self.helper_left(node.left) + self.helper_left(node.right)

    def helper_right(self, node):
        # if the node is empty, add a null to the return list
        if node is None:
            return [None]

        # add the node's value and proceed to the right node and then left node
        return [node.val] + self.helper_right(node.right) + self.helper_right(node.left)
