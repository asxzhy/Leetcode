"""
This solution uses a iterative approach. It iterate through each node in the
tree and track their level information. Update the max_level variable as we
approach deeper nodes.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        # if the tree is empty, return 0
        if root is None:
            return 0

        # this list stores all the nodes that needs to be processed
        nodes = [(root, 1)]
        # used to store the max level
        max_level = 0

        # while there are nodes left to process
        while nodes:
            # get the node and it's level information
            node, level = nodes.pop(0)
            # update the max level if needed
            max_level = max(max_level, level)

            # if there is left node or right node exist, add the node to the
            # process list and add the level by 1
            if node.left is not None:
                nodes.append((node.left, level + 1))
            if node.right is not None:
                nodes.append((node.right, level + 1))

        return max_level
