from .solution_3 import Solution
from .solution_3 import TreeNode


def test_is_subtree_case_one():
    # tree [3, 4, 5, 1, 2]
    s = TreeNode(
        3,
        TreeNode(4, TreeNode(1), TreeNode(2)),
        TreeNode(5),
    )

    # tree [4, 1, 2]
    t = TreeNode(4, TreeNode(1), TreeNode(2))

    res = Solution().is_subtree(s, t)

    assert res is True


def test_is_subtree_case_two():
    # tree [3, 4, 5, 1, 2, null, null, null, null, 0]
    s = TreeNode(
        3,
        TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))),
        TreeNode(5),
    )

    # tree [4, 1, 2]
    t = TreeNode(4, TreeNode(1), TreeNode(2))

    res = Solution().is_subtree(s, t)

    assert res is False


def test_is_subtree_case_three():
    # tree [1, 1]
    s = TreeNode(1, TreeNode(1))

    # tree [1]
    t = TreeNode(1)

    res = Solution().is_subtree(s, t)

    assert res is True


def test_is_subtree_case_four():
    # tree [12]
    s = TreeNode(12)

    # tree [2]
    t = TreeNode(2)

    res = Solution().is_subtree(s, t)

    assert res is False
