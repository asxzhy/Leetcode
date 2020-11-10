"""
This solution's concept is same as the solution one but get rid of the nested
for loop.
"""


class Solution:
    def destCity(self, paths) -> str:
        # create two variables to store all the departure city and destination
        departure = []
        destination = []
        # used to store the final result
        res = ""

        # store all the cities correspondingly
        for cities in paths:
            departure.append(cities[0])
            destination.append(cities[1])

        # the unique destination will be the final result
        for place in destination:
            if place not in departure:
                res = place

        return res
