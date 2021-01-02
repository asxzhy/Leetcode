"""
This solution iterate through the tree in level order traversal. Keeps track of
the current depth as it goes through every level in the tree.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def max_depth(self, root: "Node") -> int:
        # check if the tree exist
        if not root:
            return 0

        # set the initial depth to 0
        depth = 0
        # this list acts like a queue, it stores all the nodes in one level
        # it starts from the root level
        queue = [root]
        while queue:
            # get the number of nodes in the current level
            size = len(queue)

            # proceed to every node in the level
            for _ in range(size):
                # get the node
                node = queue.pop(0)

                # if the node has children, add them to the list
                if node.children:
                    queue += node.children

            # after a level is finished, add one to the depth
            depth += 1

        return depth
