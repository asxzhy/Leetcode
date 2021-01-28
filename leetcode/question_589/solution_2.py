"""
This solution is similar to the first solution but used an iterative way of
solving the problem.
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        # check if the tree is empty
        if not root:
            return []

        # create a list to store all the nodes' value
        lst = []
        # create a list which is used as a stack
        stack = [root]
        while stack:
            # get the node from the top of the stack
            node = stack.pop()

            # if the node exists
            if node:
                # add the node's value to the list
                lst.append(node.val)

                # add all the children of the node to the list
                if node.children:
                    for child in node.children[::-1]:
                        stack.append(child)

        return lst
