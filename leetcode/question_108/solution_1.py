"""
This solution uses a recursive function to approach the solution. Every time
the function calls itself, it get the mid point of the array and separate the
list to left and right array list and call the function again with the two new
arrays
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_BST(self, nums) -> TreeNode:
        # checks if the array is empty
        if not nums:
            return

        # get the midpoint and create a node with the midpoint's value
        mid = len(nums) // 2
        node = TreeNode(nums[mid])

        # call the function again with the sub-array and attach those nodes
        # as the left and right node
        node.left = self.sorted_array_to_BST(nums[0:mid])
        node.right = self.sorted_array_to_BST(nums[mid + 1 :])

        return node
