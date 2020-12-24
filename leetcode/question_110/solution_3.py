"""
This solution is a better version of the solution 2.
The recursive function stops when it finds one unbalanced subtree in the tree.
Whereas the second solution will keep proceed to the other subtrees until all
the nodes in the tree are visited.
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

        # check the left subtree
        is_left_balanced, left_depth = self.check(node.left)

        # if the left subtree is not balanced, there is no need to proceed
        if not is_left_balanced:
            return False, 0

        # check the right subtree
        is_right_balanced, right_depth = self.check(node.right)

        # if the right subtree is not balanced, there is no need to proceed
        if not is_right_balanced:
            return False, 0

        # the current tree is balanced when its left and right subtree's depth
        # difference is not greater than 1
        # the depth is the max depth of its left and right subtree plus one
        return abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1
