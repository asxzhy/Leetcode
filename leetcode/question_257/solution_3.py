"""
This solution uses a recursive function. Unlike the first solution which the
function keeps track of the node's path's index, this solution keeps track of
the current path as it goes through the tree, and add its path when reached
the leaf node
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binary_tree_paths(self, root: TreeNode):
        # create a list to store all the paths
        all_paths = []

        # uses a depth-first search to keep track of all its path, and store
        # the path to the all_paths list when reach leaf node
        def dfs(node, path):
            # check if the node is empty
            if not node:
                return

            # add the node's value to the path
            path += "->" + str(node.val)

            # if reached a leaf node, add its path to the list
            if not node.left and not node.right:
                all_paths.append(path[2:])
                return

            # proceed to the left and right node with its current path
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return all_paths
