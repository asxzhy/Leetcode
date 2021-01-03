"""
This solution uses a recursive function to compare each node in the s and t
tree. This recursive function first finds the node in the s tree which has the
same value as the root of the t tree. From this point the subtree of the s tree
may have the same structure to the t tree. Then the recursive function starts
to check the s and t tree's nodes to see if they have the same structure and
values.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        def helper(main: TreeNode, sub: TreeNode, found: bool) -> bool:
            # check if the two nodes are empty.
            # 1) if both nodes are empty, return True if we found the subtree
            # of main that is potentially same as the sub tree
            # 2) if one of the node is empty, return False
            if not main and not sub:
                return found
            if not main or not sub:
                return False

            # if we haven't found the node where the main tree's subtree is
            # potentially same as the sub tree
            if not found:
                # if the node in the main tree is same as the root of the sub
                # then there are two possibilities:
                # 1) starting from this node in the main tree. The tree starts
                # to be the same as the sub.
                # 2) the structure is not the same from this node because there
                # is a sub-node with the same value. eg. [1, 1] and [1]
                if main.val == sub.val:
                    return (
                        helper(main.left, sub.left, True)
                        and helper(main.right, sub.right, True)
                    ) or (
                        helper(main.left, sub, False) or helper(main.right, sub, False)
                    )
                else:
                    # if we do not find the same node, proceed to the next ones
                    return helper(main.left, sub, found) or helper(
                        main.right,
                        sub,
                        found,
                    )

            # if we found the node where the subtree of the main tree and the
            # sub tree starts to be the same
            if found:
                if main.val != sub.val:
                    return False

                return helper(main.left, sub.left, found) and helper(
                    main.right,
                    sub.right,
                    found,
                )

        return helper(s, t, False)
