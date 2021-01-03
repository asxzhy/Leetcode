from .solution_1 import Solution
from .solution_1 import TreeNode


def test_find_mode():
    third = TreeNode(2)
    second = TreeNode(2, third)
    first = TreeNode(1, None, second)

    mode = Solution().find_mode(first)

    assert mode == [2]


def test_find_mode_two_modes():
    # tree [6, 2, 8, 0, 4, 7, 9, null, null, 2, 6]
    root = TreeNode(
        6,
        TreeNode(
            2,
            TreeNode(0),
            TreeNode(4, TreeNode(2), TreeNode(6)),
        ),
        TreeNode(
            8,
            TreeNode(7),
            TreeNode(9),
        ),
    )

    mode = Solution().find_mode(root)

    assert mode == [6, 2]


def test_find_mode_empty():
    mode = Solution().find_mode(None)

    assert mode == []
