"""
Same code as the privous one, but used map and list() instead of a for loop
to get the list. This solution is much faster than the previous one.
From sample 100ms submission in leetcode.
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # add a whitespace to where the number changes
        s = s.replace("01", "0 1")
        s = s.replace("10", "1 0")

        # split the number according to the whitespace and get the length
        # of each segment
        groups = list(map(len, s.split()))
        result = 0

        for i in range(1, len(groups)):
            # add the smaller length to the final result
            result += min(groups[i - 1], groups[i])

        return result
