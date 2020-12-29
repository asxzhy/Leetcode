"""
This solution is same as the second solution but ensures the node p's value is
greater than the node q's value. Then we could remove the max() and min()
functions.
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
        # force the node p's value to be greater than the node q's value
        if p.val < q.val:
            p, q = q, p

        if root.val > p.val:
            return self.lowest_common_ancestor(root.left, p, q)
        if root.val < q.val:
            return self.lowest_common_ancestor(root.right, p, q)

        return root
