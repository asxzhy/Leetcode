"""
This solution uses a recursive function to solve the problem. This solution
finds minimum depth between the two children, and stops until it finds a node
with no child.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: TreeNode) -> int:
        # check if the node is empty
        if not root:
            return 0

        # if the node does not have child, return 1
        if not root.left and not root.right:
            return 1

        # if the node only have a left node, proceed to the left node
        if not root.right:
            return self.minDepth(root.left) + 1

        # if the node only have a right node, proceed to the right node
        if not root.left:
            return self.minDepth(root.right) + 1

        # get the min depth between the left and right node
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
