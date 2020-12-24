"""
This solution uses a while loop to add all the node values according to
level order traversal
"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        # get all the values in the p and q tree
        p_values = self.get_all_node_values(p)
        q_values = self.get_all_node_values(q)

        if p_values == q_values:
            return True
        else:
            return False

    def get_all_node_values(self, tree):
        # if the tree is empty, return an empty list
        if tree is None:
            return []

        # create a list to store all the nodes' value
        # and a list to track the next node to visit
        all_nodes = [tree.val]
        next_nodes = [tree.left, tree.right]
        while len(next_nodes) != 0:
            # get the next node
            node = next_nodes[0]

            # if the node is empty, remove it and add a null to the all_nodes
            # list. If it is not, remove the node, add its left and right node,
            # and add its value to the all_nodes list
            if node is None:
                all_nodes.append(None)
                next_nodes.pop(0)
            else:
                all_nodes.append(node.val)
                next_nodes += [node.left, node.right]
                next_nodes.pop(0)

        # remove all the null and the end of the list
        while all_nodes[len(all_nodes) - 1] is None:
            all_nodes.pop()

        # return all the nodes' value
        return all_nodes
