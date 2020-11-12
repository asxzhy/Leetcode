"""
This solution records all the coordinates and looks for the duplicate
coordinate
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # initialize a list to store all the coordinates
        positions = [[0, 0]]
        # the current coordinate
        current = [0, 0]

        for p in path:
            # make the move
            if p == "N":
                current[1] += 1
            elif p == "S":
                current[1] -= 1
            elif p == "E":
                current[0] += 1
            else:
                current[0] -= 1

            # if the current coordinate is in the positions list, then we have
            # crossed
            if current in positions:
                return True

            # add the current coordinate to the list
            positions.append(current[:])

        return False
