from .solution_1 import Solution
from .solution_1 import TreeNode


# this function is used to convert a binary tree to a string represented tree
def preorder(node: TreeNode) -> str:
    if not node:
        return " null "

    return f" {node.val} {preorder(node.left)}{preorder(node.right)}"


def test_trim_bst_case_one():
    # tree [1, 0, 2]
    root = TreeNode(1, TreeNode(0), TreeNode(2))

    res = Solution().trim_bst(root, 1, 2)

    # tree [1, null, 2]
    ans = TreeNode(1, None, TreeNode(2))

    assert preorder(res) == preorder(ans)


def test_trim_bst_case_two():
    # tree [3, 0, 4, null, 2, null, null, 1]
    root = TreeNode(
        3,
        TreeNode(0, None, TreeNode(2, TreeNode(1))),
        TreeNode(4),
    )

    res = Solution().trim_bst(root, 1, 3)

    # tree [3, 2, null, 1]
    ans = TreeNode(3, TreeNode(2, TreeNode(1)), None)

    assert preorder(res) == preorder(ans)


def test_trim_bst_case_three():
    # tree [1]
    root = TreeNode(1)

    res = Solution().trim_bst(root, 1, 2)

    assert preorder(res) == preorder(root)


def test_trim_bst_case_four():
    # tree [1, null, 2]
    root = TreeNode(1, None, TreeNode(2))

    res = Solution().trim_bst(root, 1, 3)

    assert preorder(res) == preorder(root)


def test_trim_bst_case_five():
    # tree [1, null, 2]
    root = TreeNode(1, None, TreeNode(2))

    res = Solution().trim_bst(root, 2, 4)

    assert preorder(res) == preorder(TreeNode(2))
