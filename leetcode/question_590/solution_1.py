"""
This solution uses a recursive function to ge through each node. Then add all
the nodes' value in postorder
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        # check if the node exists
        if not root:
            return []

        # create a list to store all the children of the node in postorder
        lst = []

        # if the node has children, add then to the list
        if root.children:
            for child in root.children:
                lst += self.postorder(child)

        # return the list of the node's children and itself
        return lst + [root.val]
