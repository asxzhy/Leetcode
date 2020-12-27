"""
This solution uses the same thought to solve the problem, but used a recursive
function to do it.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowest_common_ancestor(
        self,
        root: "TreeNode",
        p: "TreeNode",
        q: "TreeNode",
    ) -> "TreeNode":
        # proceed to the left subtree if the nodes are smaller than the nodes
        if root.val > max(p.val, q.val):
            return self.lowest_common_ancestor(root.left, p, q)
        # proceed to the right subtree if the nodes are greater than the nodes
        if root.val < min(p.val, q.val):
            return self.lowest_common_ancestor(root.right, p, q)

        return root
