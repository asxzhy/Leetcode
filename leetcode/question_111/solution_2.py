"""
This solution does through the level order traversal. It finds the first node
with no child and that node will be the node's depth will be the min depth.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: TreeNode) -> int:
        # check if the tree is empty
        if not root:
            return 0

        # do a level order traversal. The first node that does not have a child
        # will be the node at the min depth
        queue = [root]
        depth = 1
        while len(queue) != 0:
            size = len(queue)

            for _ in range(size):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1


s = Solution()
a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(3)
d = TreeNode(2, b, a)
e = TreeNode(1, d, c)

print(s.minDepth(e))
