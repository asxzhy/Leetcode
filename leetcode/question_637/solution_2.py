"""
This solution use a recursive function to go through every node in the tree,
and record every level's sum and total node. Then, it compute the average value
in each level using that information.
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def average_of_levels(self, root: TreeNode) -> List[float]:
        def level_order(
            node: TreeNode,
            level: int,
            arr: List[List[int]],
        ) -> None:
            # if the node does not exist, return
            if not node:
                return

            # if we are one level deeper, we increase the size of the array
            if len(arr) < level + 1:
                arr.append([node.val, 1])
            else:
                # add the node's value to the sum and node count in the list
                arr[level][0] += node.val
                arr[level][1] += 1

            # proceed to the sub-nodes
            level_order(node.left, level + 1, arr)
            level_order(node.right, level + 1, arr)

        # create a list to store the level information
        levels = []
        level_order(root, 0, levels)
        return [level[0] / level[1] for level in levels]
