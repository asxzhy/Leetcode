"""
This solution used a recursion to get all the node values according to the
preorder traversal of the binary tree and compares them
"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        # get all the values in p and q
        p_values = self.get_all_node_values(p)
        q_values = self.get_all_node_values(q)

        # remove all the null at the end of the lists
        while len(p_values) > 0 and p_values[-1] is None:
            p_values.pop(-1)
        while len(q_values) > 0 and q_values[-1] is None:
            q_values.pop(-1)

        if p_values == q_values:
            return True
        return False

    def get_all_node_values(self, node):
        # if the node is empty return null
        if node is None:
            return [None]

        # add the node's value and the subtree's values to the list
        return [node.val] + self.get_all_node_values(node.left) + \
               self.get_all_node_values(node.right)
