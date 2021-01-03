"""
This solution created a helper recursive function to go through the tree and
record every node's frequency.
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_mode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        # create a dictionary to store each node's frequency
        frequency = dict()
        # used to keep track of the maximum frequency
        max_freq = 0

        def helper(node: TreeNode) -> None:
            # bin the the variable to the nearest non-global variable max_freq
            # so I can modify the variable as the function go through the tree
            nonlocal max_freq

            # if the node is not empty
            if node:
                # check if the node is duplicated. If so, add its frequency by
                # one. If not, set its frequency to one
                if node.val in frequency:
                    frequency[node.val] += 1
                else:
                    frequency[node.val] = 1

                # check if the frequency is the current max frequency
                if frequency[node.val] > max_freq:
                    max_freq = frequency[node.val]

                # proceed to the children of the node
                helper(node.left)
                helper(node.right)

        # call the function and get the result by iterating through the
        # dictionary
        helper(root)
        res = []
        for key, value in frequency.items():
            if value == max_freq:
                res.append(key)

        return res
