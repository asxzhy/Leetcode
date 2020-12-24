"""
This solution keeps track of the depth of the tree while checking if the tree
is balanced. Whereas the first solution finds the height whenever it proceed
to a new node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: TreeNode) -> bool:
        # call the check function and return its is balanced variable
        return self.check(root)[0]

    def check(self, node):
        # check if the node is empty
        if not node:
            return True, 0

        # check the left and right subtree
        is_left_balanced, left_depth = self.check(node.left)
        is_right_balanced, right_depth = self.check(node.right)

        # the current tree is balanced only when its left and right subtree are
        # balanced and their depth is not greater than 1
        # the depth is the max depth of its left and right subtree plus one
        return (
            is_left_balanced
            and is_right_balanced
            and abs(left_depth - right_depth) <= 1,
            max(left_depth, right_depth) + 1,
        )
