"""
This solution uses a recursive function to go through each path in the tree
and check if any path has a total value equal to the sum
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        # check if the node is empty
        if not root:
            return False

        def find_sum(node, total):
            # if it is a leaf node, check if the sum is equal to all the nodes'
            # value on the path
            if not node.left and not node.right:
                return (total + node.val) == sum

            # check if the left or right path has a total sum equal to the
            # input sum
            left, right = False, False
            if node.left:
                left = find_sum(node.left, total + node.val)
            if node.right:
                right = find_sum(node.right, total + node.val)

            return left or right

        return find_sum(root, 0)
