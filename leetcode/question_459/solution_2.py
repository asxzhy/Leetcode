"""
from discussion in leetcode. we add two input string together, but remove its
first and last element. Then find the input string in this new sting, if we can
find the string that means there are repeated substrings in the input string.
"""


class Solution:
    def repeated_substring_pattern(self, s: str) -> bool:
        ss = (s + s)[1:-1]

        return ss.find(s) != -1
