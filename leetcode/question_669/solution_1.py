"""
This solution uses a recursive function to go through each node using postorder
traversal. It checks if each node's value is in the bound. If not it returns
the correct node the parent should attach to.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # if the node does not exist, return null
        if not root:
            return None

        # proceed to the left and right child
        root.left = self.trim_bst(root.left, low, high)
        root.right = self.trim_bst(root.right, low, high)

        # if the node's value is in the bound, return itself
        # if the node's value is not in the bound, return the left or right
        # child if there is one.
        # the children of the node is in the bound because the child is
        # evaluate and changed first
        if low <= root.val <= high:
            return root
        else:
            if root.left:
                return root.left
            if root.right:
                return root.right

            return None
