"""
This solution uses the set instead of the list in the solution 2 since
set is faster the list
"""


class Solution:
    def destCity(self, paths) -> str:
        # create two variables to store all the departure city and destination
        departure = set()
        destination = set()
        # used to store the final result
        res = ""

        # store all the cities correspondingly
        for cities in paths:
            departure.add(cities[0])
            destination.add(cities[1])

        # the unique destination will be the final result
        for place in destination:
            if place not in departure:
                res = place

        return res
