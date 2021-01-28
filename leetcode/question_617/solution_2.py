"""
This solution does not creates a new tree to solve the problem. Instead, it
modifies the tree 1 to be the merged tree. It uses an iterative approach to
go through every node in the two trees at the same time and modifies the
tree 1's node to be the new merged node
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # if t1 does not exist, return t2. T2 could be a null or an existing
        # node
        if not t1:
            return t2

        # create a list to store both trees' node like a stack
        stack = [(t1, t2)]
        while stack:
            # get the two nodes
            trees = stack.pop()

            # if the tree 2 does not exist, continue to the next node because
            # there is no need to change the tree 1
            if not trees[1]:
                continue

            # if both tree exist, change the tree 1's node to have the sum
            trees[0].val += trees[1].val

            # if the tree 1's node does not have a left child, attach the tree
            # 2's left child to it.
            # else add the two left sub nodes to the stack
            if not trees[0].left:
                trees[0].left = trees[1].left
            else:
                stack.append((trees[0].left, trees[1].left))

            # if the tree 1's node does not have a right child, attach the tree
            # 2's right child to it.
            # else add the two right sub nodes to the stack
            if not trees[0].right:
                trees[0].right = trees[1].right
            else:
                stack.append((trees[0].right, trees[1].right))

        # return the changed tree 1
        return t1
