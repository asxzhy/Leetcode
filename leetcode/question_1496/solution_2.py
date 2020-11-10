"""
This solution is same as the solution 1 but used set instead of list
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # initialize a set to store all the positions
        positions = {(0, 0)}
        # create the x, y coordinates
        x = y = 0

        for p in path:
            # make the move
            if p == "N":
                y += 1
            elif p == "S":
                y -= 1
            elif p == "E":
                x += 1
            else:
                x -= 1

            # check if the current coordinate is in the positions set
            if (x, y) in positions:
                return True

            # add the current coordinate to the set
            positions.add((x, y))

        return False
