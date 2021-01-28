"""
This solution uses a recursive function to go through each node in the tree
and calculates the value each node's value needs in order to sum up to k.
Then look for those values as it goes through each node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_target(self, root: TreeNode, k: int) -> bool:
        # create a set to store the complement of a value to k
        # eg. k = 3, node.val = 2 -> complement = 1
        complement = set()

        def helper(node: TreeNode) -> bool:
            # check if the node exists
            if not node:
                return False

            # if the node's value is in the list, return True
            if node.val in complement:
                return True

            # add the current node's value's complement to the list
            complement.add(k - node.val)
            # proceed to the left and right child
            return helper(node.left) or helper(node.right)

        return helper(root)
