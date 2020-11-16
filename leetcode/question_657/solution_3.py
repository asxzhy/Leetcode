"""
compare the total number of two opposite directions. If They are the same then
that means the robot did not move
"""


class Solution:
    def judge_circle(self, moves: str) -> bool:
        # check if there is the same amount of opposite direction in the
        # input string
        return moves.count("U") == moves.count("D") and moves.count("R") == moves.count(
            "L",
        )
