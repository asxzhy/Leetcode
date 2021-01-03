from .solution_1 import Solution
from .solution_1 import TreeNode


def test_min_diff_case_one():
    # tree [1, null, 3, 2]
    root = TreeNode(1, None, TreeNode(3, TreeNode(2)))

    res = Solution().get_minimum_difference(root)

    assert res == 1


def test_min_diff_case_two():
    # tree [236, 104, 701, null, 227, null, 911]
    root = TreeNode(
        236,
        TreeNode(104, None, TreeNode(227)),
        TreeNode(701, None, TreeNode(911)),
    )

    res = Solution().get_minimum_difference(root)

    assert res == 9
