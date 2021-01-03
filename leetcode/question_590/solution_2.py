"""
This solution uses an iterative approach to solve the problem. It adds all the
nodes' value in reverse of the postorder, then reverse the list back when
returning.
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        # check if the tree is empty
        if not root:
            return []

        # create a list to store the answer
        lst = []
        # create a list that is used as a stack
        stack = [root]

        # add all the nodes' value in the reverse order of postorder
        while stack:
            # get the node
            node = stack.pop()

            # if the node has children, add them to the stack
            if node.children:
                stack.extend(node.children)

            # add the node's value to the list
            lst.append(node.val)

        # reverse the list to get the postorder traversal
        return lst[::-1]
