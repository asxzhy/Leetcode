"""
Path[i] contains [city1, city2]. city1 is always going to be the departure city
and the city 2 is always going to be the destination. Therefore, only city2 is
possible to be the final destination. If a city2 is not the final destination,
then there have to be a city1 same to the city2. This solution uses this
concept to solve this question
"""


class Solution:
    def destCity(self, paths) -> str:
        # the variable will be storing the final destination
        destination = ""

        # iterate through all the paths, look for the unique paths[i][1]
        for i in range(len(paths)):
            for y in range(len(paths)):
                if paths[i][1] == paths[y][0]:
                    break
            else:
                # if the for loop does not break then that means path[i][01]
                # is the final destination
                destination = paths[i][1]

        return destination
