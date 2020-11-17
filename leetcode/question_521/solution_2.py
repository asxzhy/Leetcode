"""
Two possibilities:
1. two input strings are exactly the same;
2. input strings are not the same (even with one letter difference),
return the longer input's length
"""


class Solution:
    def find_LUS_length(self, a: str, b: str) -> int:
        if a == b:
            return -1

        return max(len(a), len(b))
