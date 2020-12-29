"""
Since the input tree is a Binary Search Tree, we compare the node's value with
the two input node's value to find where to proceed.
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
        # while we have not reached the root, do the algorithm
        while root:
            # 1) If the root's value is less than p's and q's value,
            # then the p and q node are at the left subtree
            # 2) fi the root's value is greater than p's and q's value,
            # then the p and q node are at the right subtree
            # 3) if the p or q's value equal to the current node's value, or
            # the p and q node is at different subtree of the current node.
            # Then the node is the common ancestor
            if root.val > max(p.val, q.val):
                root = root.left
            elif root.val < min(p.val, q.val):
                root = root.right
            else:
                return root
