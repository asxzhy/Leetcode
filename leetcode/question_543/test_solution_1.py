from .solution_1 import Solution
from .solution_1 import TreeNode


def test_diameter_case_one():
    # tree [1, 2, 3, 4, 5]
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3),
    )

    res = Solution().diameter_of_binary_tree(root)

    assert res == 3
