from .solution_1 import Solution
from .solution_1 import TreeNode


def test_find_tilt_case_one():
    # tree [1, 2, 3]
    root = TreeNode(1, TreeNode(2), TreeNode(3))

    res = Solution().find_tilt(root)

    assert res == 1


def test_find_tilt_case_two():
    # tree [4, 2, 9, 3, 5, null, 7]
    root = TreeNode(
        4,
        TreeNode(2, TreeNode(3), TreeNode(5)),
        TreeNode(9, None, TreeNode(7)),
    )

    res = Solution().find_tilt(root)

    assert res == 15


def test_find_tilt_case_three():
    # tree [21, 7, 14, 1, 1, 2, 2, 3, 3]
    root = TreeNode(
        21,
        TreeNode(
            7,
            TreeNode(1, TreeNode(3), TreeNode(3)),
            TreeNode(1),
        ),
        TreeNode(
            14,
            TreeNode(2),
            TreeNode(2),
        ),
    )

    res = Solution().find_tilt(root)

    assert res == 9
