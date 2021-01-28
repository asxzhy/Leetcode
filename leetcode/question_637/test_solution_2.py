from .solution_2 import Solution
from .solution_2 import TreeNode


def test_average_of_levels_case_one():
    # tree [3, 9, 20, null, null, 15, 7]
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )

    res = Solution().average_of_levels(root)

    assert res == [3, 14.5, 11]
