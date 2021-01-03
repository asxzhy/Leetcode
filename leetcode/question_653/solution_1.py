"""
This solution stores all the values in the tree to a list in ascending order.
Then it uses a two pointer to check all the possible combinations of two
value's sum, and check if there are two values sum up to k
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_target(self, root: TreeNode, k: int) -> bool:
        # create a list to store all the nodes' value in ascending order
        values = []

        # add all the nodes' value using inorder traversal to the list
        def inorder(node: TreeNode) -> None:
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        # if there is only one node, return false
        if len(values) == 1:
            return False

        # use a two pointer to find if there is two number's sum equal to k
        lp = 0
        rp = 1
        while lp < len(values) - 1:
            # if the two value's sum equal to k, return True
            if values[lp] + values[rp] == k:
                return True

            # if the two value's sum is greater, increase left pointer by 1
            if values[rp] + values[lp] > k:
                lp += 1
                rp = lp + 1
            elif rp < len(values) - 1:
                # if the right pointer won't not out of index, increase it by 1
                rp += 1
            else:
                # if the right pointer will be out of index, increase left
                # pointer by 1 and set the right pointer to be at the index to
                # the right by 1
                lp += 1
                rp = lp + 1

        return False
