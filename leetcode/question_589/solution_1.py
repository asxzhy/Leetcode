"""
This solution uses a recursive function to solve the problem. It visits all the
nodes in the tree using preorder traversal and return the values in a list.
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        # check if the node exists
        if not root:
            return []

        # create a list to store the values using preorder traversal for the
        # node's children
        lst = []
        # if the node has children, add them into the list
        if root.children:
            for child in root.children:
                lst += self.preorder(child)

        # return the node's value and its children
        return [root.val] + lst
