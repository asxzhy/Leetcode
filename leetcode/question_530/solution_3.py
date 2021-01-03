"""
This solution creates an list which contains all the values in ascending order,
and compute the minimum difference by iterating through the list.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(self, root: TreeNode) -> int:
        # this list will store all the values in the tree in ascending order
        values = []

        # visit the nodes using inorder traversal. The order that every node is
        # visited will be in ascending order.
        def inorder_traversal(node: TreeNode):
            if node:
                if node.left:
                    inorder_traversal(node.left)

                values.append(node.val)

                if node.right:
                    inorder_traversal(node.right)

        inorder_traversal(root)
        # get the difference between every value and get the minimum difference
        return min(values[i + 1] - values[i] for i in range(len(values) - 1))
