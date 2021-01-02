"""
This solution goes through the BST using inorder traversal and record the
previously visited node as it iterate through the tree. The previously visited
node is the greatest node that is smaller than the current node. Compare them
and see if it's the minimum difference
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(self, root: TreeNode) -> int:
        # this variable is used to store the previously visited node
        prev = None
        # this will be storing the result for the solution
        minimum = float("inf")

        def inorder_traversal(node: TreeNode):
            if node:
                nonlocal minimum
                nonlocal prev

                # go to the left node if there is one
                if node.left:
                    inorder_traversal(node.left)

                # if the node is not the first visited node, get the difference
                # and check if it's smaller than the current minimum difference
                if prev:
                    minimum = min(abs(node.val - prev.val), minimum)

                # set this node as the previous node
                prev = node

                # go to the right node if there is one
                if node.right:
                    inorder_traversal(node.right)

        inorder_traversal(root)
        return minimum
