"""
This solution uses a recursive function to iterate through every node in the
N-ary tree and keeps track of every node's maximum depth until it iterate back
to the root node and get the maximum depth of the tree.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def max_depth(self, root: "Node") -> int:
        # check if the tree is empty
        if not root:
            return 0

        def depth(node: "Node") -> int:
            # check if the node exist
            if not node:
                return 0

            # if the node has children, proceed to its children and get the max
            # depth
            if node.children:
                maximum = max(depth(child) for child in node.children)

                # return the depth plus 1 (the current node)
                return maximum + 1

            # if the node does not have any children, return 1 instead
            return 1

        return depth(root)
