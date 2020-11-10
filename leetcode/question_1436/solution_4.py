"""
Similar to solution 3
"""


class Solution:
    def destCity(self, paths) -> str:
        # create two variables to store all the departure city and destination
        departure = set()
        destination = set()

        # store all the cities correspondingly
        for cities in paths:
            departure.add(cities[0])
            destination.add(cities[1])

        # find the left city in destination is unique which is the final result
        difference = destination - departure

        return difference.pop()
