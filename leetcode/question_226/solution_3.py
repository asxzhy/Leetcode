"""
This solution is similar to solution 1 but used an iterative approach. It
iterates through every node in the tree and switch the node's children.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        # this list will temporarily store all the nodes in the tree
        nodes = [root]
        while nodes:
            # gets the first node in the list
            node = nodes.pop(0)

            # if the node is not empty, switch the node's children and add its
            # children to the list
            if node:
                node.left, node.right = node.right, node.left
                nodes += [node.left, node.right]

        return root
