from .solution_2 import Node
from .solution_2 import Solution


def test_max_depth_case_one():
    # N-ary Tree is represented in their level order traversal, each group of
    # children is separated by the null value

    # tree [1, null, 3, 2, 4, null, 5, 6]
    root = Node(
        1,
        [
            Node(3, [Node(5), Node(6)]),
            Node(2),
            Node(4),
        ],
    )

    res = Solution().max_depth(root)

    assert res == 3


def test_max_depth_case_two():
    # tree [1, null, 2, 3, 4, 5,null, null, 6, 7, null, 8, null, 9, 10, null,
    # null, 11, null, 12, null, 13, null, null, 14]
    root = Node(
        1,
        [
            Node(2),
            Node(
                3,
                [
                    Node(6),
                    Node(7, [Node(11, [Node(14)])]),
                ],
            ),
            Node(
                4,
                [Node(8, [Node(12)])],
            ),
            Node(
                5,
                [
                    Node(9, [Node(13)]),
                    Node(10),
                ],
            ),
        ],
    )

    res = Solution().max_depth(root)

    assert res == 5
