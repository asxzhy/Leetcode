"""
Create a (x, y) coordinate for the robot, move left will decrease the x by one,
right will increase the x by one. Same process for y coordinate
"""


class Solution:
    def judge_circle(self, moves: str) -> bool:
        position = [0, 0]  # used to keep track of the robot's position

        for d in moves:
            # add and subtract the robot's coordinate according to the letter
            if d == "R":
                position[0] += 1
            elif d == "L":
                position[0] -= 1
            elif d == "U":
                position[1] += 1
            elif d == "D":
                position[1] -= 1

        # check if the robot return to the origin
        return position == [0, 0]
