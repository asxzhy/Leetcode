"""
This solution is similar to the second solution but used a recursive function
to get the string of the tree's preorder traversal. Then checks if the t tree
is a subtree of the s tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preorder_string(node: TreeNode) -> str:
            # if the node does not exist, return a null
            if not node:
                return " null "

            # return the node's value and is children's value using preorder
            # traversal
            return (
                f" {node.val} "
                f"{preorder_string(node.left)}"
                f"{preorder_string(node.right)}"
            )

        # check if the t tree is a subtree of the s tree
        return preorder_string(t) in preorder_string(s)
