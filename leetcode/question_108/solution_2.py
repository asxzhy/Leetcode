"""
Modified the solution 2 after seeing other people's faster submission.
This solution passes a left and right pointer instead of new list as parameters
However, it seems those two solutions are about the same speed
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_BST(self, nums) -> TreeNode:
        def helper(left, right):
            # if the left pointer is greater than the right pointer, then exit
            if left > right:
                return None

            # get the mid point and create a new node with the nums a at index
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # call the function again with a fewer range to get it's children
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)

            return node

        return helper(0, len(nums) - 1)
