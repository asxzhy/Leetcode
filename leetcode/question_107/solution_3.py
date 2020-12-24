"""
This solution is similar to solution 1 but it's more clear and easier to
understand
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_bottom(self, root: TreeNode):
        # check if the binary tree is empty
        if not root:
            return []

        res = []  # it stores the result
        queue = [root]  # it stores all the nodes needed to be proceed later
        while len(queue) != 0:
            # get the size of the queue (the size of the current level)
            size = len(queue)
            # set the level to empty
            level = []

            # loop through the current level and add all the node's value to
            # the variable level and add any children to the list names queue
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # insert the list to the front of the res list
            res.insert(0, level)

        return res
