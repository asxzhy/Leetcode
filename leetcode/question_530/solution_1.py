"""
This solution goes through the Binary Search Tree using inorder traversal
and compare the node's value with every previous node'e value to find the
minimum difference
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(self, root: TreeNode) -> int:
        # this list is used to store the previously visited nodes
        values = []
        # set a variable to store the minimum difference and give it an
        # infinite initial value
        minimum = float("inf")

        # access the BST using inorder traversal
        def inorder_traversal(node: TreeNode):
            if node:
                nonlocal minimum

                inorder_traversal(node.left)

                # if the values is not empty, get the difference to every value
                # in the list and get the smallest difference.
                # compare the difference to see if it's the minimum difference
                if values:
                    diff = min(abs(node.val - val) for val in values)
                    minimum = min(diff, minimum)

                # add the node's value to the values list
                values.append(node.val)

                inorder_traversal(node.right)

        inorder_traversal(root)
        return minimum
