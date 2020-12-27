"""
This solution uses a level order traversal to go through all the nodes in the
tree and record all the paths from root to leaf
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binary_tree_paths(self, root: TreeNode):
        # check if the tree is emtpy
        if not root:
            return []

        # create a list to store all the paths
        all_paths = [""]
        # create a list with the functionality of a queue to store
        # all the nodes needed to be visited and its path's index
        queue = [(root, 0)]
        while queue:
            size = len(queue)

            for _ in range(size):
                # get the node and its path's index
                node, index = queue.pop(0)

                # 1) if it is a leaf node, add its value to its path
                # 2) if the node only have a left child, add its value and
                # proceed to the left child
                # 3) if the node only have a right child, add its value and
                # proceed to the right child
                # 4) if the node has two children, add its value and duplicate
                # its path for its second child to keep recording its path
                if not node.left and not node.right:
                    all_paths[index] += str(node.val)
                elif not node.right:
                    all_paths[index] += str(node.val) + "->"
                    queue.append((node.left, index))
                elif not node.left:
                    all_paths[index] += str(node.val) + "->"
                    queue.append((node.right, index))
                else:
                    all_paths[index] += str(node.val) + "->"
                    all_paths.append(all_paths[index])

                    queue.append((node.left, index))
                    queue.append((node.right, len(all_paths) - 1))

        return all_paths
