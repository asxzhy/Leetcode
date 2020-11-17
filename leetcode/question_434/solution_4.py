"""
After getting rid of the variable, prev, this solution's runtime and memory
usage is still the same as the solution three.
"""


class Solution:
    def count_segments(self, s: str) -> int:
        count = 0  # used to count the number of segments

        for i in range(0, len(s)):
            # if the previous element is a space and the current one is not,
            # add count by one
            if s[i] != " " and (i == 0 or s[i - 1] == " "):
                count += 1

        return count
