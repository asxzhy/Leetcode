"""
This solution uses a recursive function to get the binary tree's level order
traversal. Then it reverse the list got from the recursive function which now
becomes the bottom-up level order traversal.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_bottom(self, root: TreeNode):
        # initialize a list to store the result list
        res = []

        # call the regular level order traversal function to get the list
        self.level_order(root, 0, res)

        # reverse the list to get the bottom-up level order traversal
        return reversed(res)

    def level_order(self, node, depth, result):
        # check if the node is empty
        if node is None:
            return

        # add one more list if the node is 1 level deeper
        if depth == len(result):
            result.append([])

        # add the value to the corresponding level
        result[depth].append(node.val)

        # call the function to process its left and right child
        self.level_order(node.left, depth + 1, result)
        self.level_order(node.right, depth + 1, result)
