"""
This solution is same as solution 1 but changed the base case and removed two
unnecessary if statements
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        # check if the node is empty
        if not root:
            return False

        def find_sum(node, total):
            # if the node is empty, return false. Leaf node's child won't go
            # into this if statement
            if not node:
                return False

            # if it is a leaf node, check if the sum is equal to all the nodes'
            # value on the path
            if not node.left and not node.right:
                return (total + node.val) == sum

            # go through the left and right path to see if either has a same
            # value as the sum
            return find_sum(node.left, total + node.val) or find_sum(
                node.right,
                total + node.val,
            )

        return find_sum(root, 0)
