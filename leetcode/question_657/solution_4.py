"""
Same method as solution one but used two int instead of a list. Just want to
see if that affects the memory usage and speed.
"""


class Solution:
    def judge_circle(self, moves: str) -> bool:
        x = 0
        y = 0

        for d in moves:
            # add and subtract the robot's coordinate according to the letter
            if d == "R":
                x += 1
            elif d == "L":
                x -= 1
            elif d == "U":
                y += 1
            elif d == "D":
                y -= 1

        # check if the robot return to the origin
        return x == 0 and y == 0
