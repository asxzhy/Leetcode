"""
This solution uses a function to iterate through a tree and create a string
with the tree's node values using preorder traversal. Then it checks if the t
tree's traversal is contained in the s tree's traversal to identify if t is s'
subtree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preorder_string(root: TreeNode) -> str:
            # the return string which stores all the nodes in the tree in
            # preorder traversal
            string = ""
            # create a list that will be used as a stack
            stack = [root]

            while stack:
                # get the node at the top of the stack
                node = stack.pop()

                # if the node exist, add the node's value to the string
                # and add the node's right and left children to the stack.
                # add the left node last so we proceed to the left child in the
                # next loop
                if node:
                    string += " " + str(node.val) + " "
                    stack += [node.right, node.left]
                else:
                    # if the node does not exist, add null
                    string += " null "

            return string

        # check if the t tree is a subtree of the s tree
        return preorder_string(t) in preorder_string(s)
