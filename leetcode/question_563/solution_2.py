"""
This solution is similar to the first solution. It changed the recursive
function to only return the sum of the subtree's value. The sum of the tilt
is recorded by an outer variable
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

        # create a variable to store the sum of tilt
        total_tilt = 0

        # this recursive function goes through every node in the tree and
        # calculate all the tilts. It returns the sum of the subtree's value
        def helper(node: TreeNode) -> int:
            # check if the node exists
            if not node:
                return 0

            # get the left and right subtree's sum
            left_sum = helper(node.left)
            right_sum = helper(node.right)

            # calculate this node's tilt and add the tilt to the sum
            nonlocal total_tilt
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt

            # return the sum of its value and its subtrees' values
            return left_sum + right_sum + node.val

        helper(root)
        return total_tilt
