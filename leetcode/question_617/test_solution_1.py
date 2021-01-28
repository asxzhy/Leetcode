from .solution_1 import Solution
from .solution_1 import TreeNode


# this function is used to convert a binary tree to a string represented tree
def preorder(node: TreeNode) -> str:
    if not node:
        return " null "

    return f" {node.val} {preorder(node.left)}{preorder(node.right)}"


def test_merge_trees_case_one():
    # tree [1, 3, 2, 5]
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    # tree [2, 1, 3, null, 4, null, 7]
    t2 = TreeNode(
        2,
        TreeNode(1, None, TreeNode(4)),
        TreeNode(3, None, TreeNode(7)),
    )

    # tree [3, 4, 5, 5, 4, null, 7]
    ans = TreeNode(
        3,
        TreeNode(4, TreeNode(5), TreeNode(4)),
        TreeNode(5, None, TreeNode(7)),
    )

    res = Solution().merge_trees(t1, t2)

    assert preorder(res) == preorder(ans)
