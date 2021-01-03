"""
This solution is similar to solution 2 but used an iterative approach instead
of using recursive funtion.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_target(self, root: TreeNode, k: int) -> bool:
        # create a set to store all the complement the node needs
        complement = set()
        stack = [root]
        while stack:
            node = stack.pop(0)

            # if the current node's value is a complement of the previous node
            # return True
            if node.val in complement:
                return True

            # add the current node's value's complement to the set
            complement.add(k - node.val)

            # proceed to the left or right child if there is one
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return False
