"""
This solution is similar to the previous solution. Instead of adding up the
path's value, it subtract every node's value as it goes through the tree and
checks if the sum is zero when reached the leaf node
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

        # the sum after subtracted by the node's value
        sum -= root.val

        # if the node is the leaf node, check if the sum is zero
        if not root.left and not root.right:
            return sum == 0

        # if we have not reached the leaf node, continue to the next nodes
        return self.has_path_sum(root.left, sum) or self.has_path_sum(root.right, sum)
