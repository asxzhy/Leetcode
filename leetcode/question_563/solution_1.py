"""
This solution uses a recursive function to visit every node in postorder
traversal, and calculate every node's tilt. It keeps the sum of the subtree's
value and sum of the tilt as the return value
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_tilt(self, root: TreeNode) -> int:
        # check if the tree exist
        if not root:
            return 0

        # this recursive function calculates every node's tilt as it goes
        # through each node in the tree.
        # It returns the sum of value and sum of tilt.
        def helper(node: TreeNode) -> [int, int]:
            # check if the node exist
            if not node:
                return [0, 0]

            # get the sum of the left and right subtree, and the sum of left
            # tilt and right tile
            left_sum, left_tilt = helper(node.left)
            right_sum, right_tilt = helper(node.right)

            # get the tilt for this node
            tilt = abs(left_sum - right_sum)

            # return the current sum of all nodes' value and the sum of tilt
            return [
                left_sum + right_sum + node.val,
                tilt + left_tilt + right_tilt,
            ]

        # return the sum of tilt
        return helper(root)[1]
