"""
This solution is similar to the first solution but used a counter instead
"""
from collections import Counter
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_mode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        # create a counter to store each node's frequency
        count = Counter()

        # go through each node in the tree and record the frequency
        def helper(node: TreeNode) -> None:
            if node:
                count[node.val] += 1

                helper(node.left)
                helper(node.right)

        helper(root)
        # get the max frequency
        max_freq = max(count.values())
        # get all the node values that have the max frequency
        return [val for val in count if count[val] == max_freq]
