"""
uses a recursive function. Base cases are when the node does not contain
anything, return nothing, and if the node is at the end, return its value.
If the node has a right node but its left node is empty, return a "()" for the
left node and then process the right node. If the node only has a left node,
go to the left node. If the node has both left and right node,
then go to the left and right node respectively.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str(self, t) -> str:
        if t is None:
            return ""

        if t.left is None and t.right is None:
            return str(t.val)

        if t.left is None:
            return str(t.val) + "()" + "(" + self.tree2str(t.right) + ")"

        if t.right is None:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"

        return (
            str(t.val)
            + "("
            + self.tree2str(
                t.left,
            )
            + ")"
            + "("
            + self.tree2str(t.right)
            + ")"
        )
