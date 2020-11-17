"""
Create a string use to store the direction of the robot, if the next direction
has an opposite direction in the stirng, then remove that direction. Check if
the robot returns to the origin by checking the length of the string
"""


class Solution:
    def judge_circle(self, moves: str) -> bool:
        m = ""  # used to store the direction of the robot

        for d in moves:
            # if the opposite direction letter is in variable m, replace that
            # letter with a empty string
            if d == "L" and "R" in m:
                m = m.replace("R", "", 1)
            elif d == "D" and "U" in m:
                m = m.replace("U", "", 1)
            elif d == "R" and "L" in m:
                m = m.replace("L", "", 1)
            elif d == "U" and "D" in m:
                m = m.replace("D", "", 1)
            else:  # if there is no opposite direction letter add the current
                # direction to the variable
                m += d

        return len(m) == 0
