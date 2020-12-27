"""
This solution modified the solution 3. It removes the unnecessary function
calls (only calls itself when there is a child)
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
        all_paths = []

        # uses a depth-first search to keep track of all its path, and store
        # the path to the all_paths list when reach leaf node
        def dfs(node, path):
            # add the node's value to the path
            path += "->" + str(node.val)

            # if reached a leaf node, add its path to the list
            if not node.left and not node.right:
                all_paths.append(path[2:])
            else:
                # proceed to the left or right child if there is one
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)

        dfs(root, "")
        return all_paths
