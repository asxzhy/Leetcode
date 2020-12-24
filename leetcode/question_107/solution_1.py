"""
This solution uses an iterative approach to get the bottom-up level order
traversal. It stores each level's values and insert the values to the front
of the result list.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_bottom(self, root: TreeNode):
        # check if the tree is empty
        if root is None:
            return []

        all_values = [[root.val]]  # store values at each level
        level_values = []  # store values at one level
        current_level = [root.left, root.right]  # store nodes for current level
        next_level = []  # store nodes for next level
        while True:
            # get the node from the current level's nodes
            node = current_level.pop(0)

            # if the node is not null, add its value to the level_values and
            # add its children to the next level
            if node is not None:
                level_values.append(node.val)
                next_level += [node.left, node.right]

            # if we finished the current level, proceed to the next level
            if len(current_level) == 0:
                # if there are no values at the current level, don't insert it
                # to the all_values list
                if level_values:
                    all_values.insert(0, level_values)
                    level_values = []

                # if there is no next level, we exit
                if not next_level:
                    break

                # set the current level to the next level, and clear the next
                # level
                current_level = next_level
                next_level = []

        return all_values
