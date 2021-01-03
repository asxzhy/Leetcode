"""
This solution goes through each node in level order and calculates the sum
in every level. Then calculates the average and store it in the result list.
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def average_of_levels(self, root: TreeNode) -> List[float]:
        # create a list to store the result
        res = []
        # create a list to store the nodes needed to be processed
        queue = [root]
        while queue:
            # get the size of the current level
            size = len(queue)
            # used to keep track of the sum of the values in the level
            total = 0

            # go through every node in the level. Add the nodes' value to the
            # total and add its children to the list
            for _ in range(size):
                node = queue.pop(0)

                total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # calculate the average and append into the res list
            res.append(total / size)

        return res
