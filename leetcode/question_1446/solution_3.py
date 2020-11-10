"""
This solution is similar to the solution 2 but uses a count to count the length
instead of compute the length.
"""


class Solution:
    def maxPower(self, s: str) -> int:
        maximum = 0  # the maximum length of unique characters' group
        count = 0  # length of a unique character group
        prev = ""  # the previous character

        # iterate through the input string and get the maximum length of the
        # unique character group
        for i in s:
            if prev == i:
                count += 1
            else:
                prev = i
                count = 1
            maximum = max(maximum, count)

        return maximum
