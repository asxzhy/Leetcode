"""
Found a interesting solution in discussion section.
Learned that a true or false statement can be seen as 1 or 0 and used to compute
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[::-1]) - (s == "")
