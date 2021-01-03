"""
This solution is same as the first solution but did not use a helper function.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def max_depth(self, root: "Node") -> int:
        # check if the node exist
        if not root:
            return 0

        # set the max depth to 0
        maximum = 0
        # proceed to every child of the node and get the max depth
        if root.children:
            maximum = max(self.max_depth(child) for child in root.children)

        # return the max depth plus 1 (the current node)
        return maximum + 1
