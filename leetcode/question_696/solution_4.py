"""
Tried to use the split method to separate the string to a list. To accomplish
this. We used replace to add a whitespace between every number change.
"""


class Solution:
    def count_binary_substrings(self, s: str) -> int:
        # add a whitespace to where the number changes
        s = s.replace("01", "0 1")
        s = s.replace("10", "1 0")

        # split the number according to the whitespace and get the length of
        # each segment
        groups = [len(i) for i in s.split()]
        result = 0

        for i in range(1, len(groups)):
            # add the smaller length to the final result
            result += min(groups[i - 1], groups[i])

        return result
