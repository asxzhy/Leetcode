"""
This solution uses an iterative method to go through every node in the tree and
look for the left leaf node and add its value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sum_of_left_leaves(self, root: TreeNode) -> int:
        # check if the tree is empty
        if not root:
            return 0

        # go through every node in the tree and check if it has a left leaf
        # node
        total = 0
        queue = [root]
        while queue:
            node = queue.pop(0)

            if node.left and not node.left.left and not node.left.right:
                # if it has a left leaf node, add the leaf node's value
                total += node.left.val
                if node.right:
                    queue.append(node.right)
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return total
