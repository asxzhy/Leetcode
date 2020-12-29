"""
This solution uses a recursive function to go through each path in the tree,
and a list outside of the recursive function to store all the path as the
recursive function goes through the binary tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binary_tree_paths(self, root: TreeNode):
        # check if the tree is empty
        if not root:
            return []

        # create a list to store all the paths
        all_paths = [""]

        # this function is used to find all the path recursively and store all
        # the paths in the all_paths list
        def find_all_paths(node, index):
            # if it is a leaf node, add the node's value to the list and return
            if not node.left and not node.right:
                all_paths[index] += str(node.val)
                return

            # if it is not a leaf node, add its value and string -> to the
            # current path
            all_paths[index] += str(node.val) + "->"

            # if the node only have a left node, proceed to the left node
            if not node.right:
                return find_all_paths(node.left, index)

            # if the node only have a right node, proceed to the right node
            if not node.left:
                return find_all_paths(node.right, index)

            # if the node has two children, store the same path to the end of
            # the all_paths list for the right node.
            all_paths.append(all_paths[index])
            # get the index for the right node's path
            new_index = len(all_paths) - 1

            # proceed to the left node
            find_all_paths(node.left, index)
            # proceed to the right node, with the new index
            find_all_paths(node.right, new_index)
            return

        find_all_paths(root, 0)
        return all_paths
