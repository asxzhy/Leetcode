from .solution_1 import Solution
from .solution_1 import TreeNode


def test_find_target_case_one():
    # tree [5, 3, 6, 2, 4, null, 7]
    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2), TreeNode(4)),
        TreeNode(6, None, TreeNode(7)),
    )

    res = Solution().find_target(root, 9)

    assert res is True


def test_find_target_case_two():
    # tree [5, 3, 6, 2, 4, null, 7]
    root = TreeNode(
        5,
        TreeNode(3, TreeNode(2), TreeNode(4)),
        TreeNode(6, None, TreeNode(7)),
    )

    res = Solution().find_target(root, 28)

    assert res is False


def test_find_target_case_three():
    # tree [2, 1, 3]
    root = TreeNode(2, TreeNode(1), TreeNode(3))

    res = Solution().find_target(root, 4)

    assert res is True


def test_find_target_case_four():
    # tree [2, 1, 3]
    root = TreeNode(2, TreeNode(1), TreeNode(3))

    res = Solution().find_target(root, 1)

    assert res is False


def test_find_target_case_five():
    # tree [2, 1, 3]
    root = TreeNode(2, TreeNode(1), TreeNode(3))

    res = Solution().find_target(root, 3)

    assert res is True


def test_find_targer_case_six():
    # tree [2, 0, 3, -4, 1]
    root = TreeNode(2, TreeNode(0, TreeNode(-4), TreeNode(1)), TreeNode(3))

    res = Solution().find_target(root, -1)

    assert res is True


def test_find_target_case_seven():
    # tree [0, -1, 2, -3, null, null, 4]
    root = TreeNode(
        0,
        TreeNode(-1, TreeNode(-3), None),
        TreeNode(2, None, TreeNode(4)),
    )

    res = Solution().find_target(root, -4)

    assert res is True


def test_find_target_case_eight():
    # tree [1, null, 2]
    root = TreeNode(1, None, TreeNode(2))

    res = Solution().find_target(root, 2)

    assert res is False
