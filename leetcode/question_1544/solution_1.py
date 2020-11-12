"""
This solution loops through the input string and remove all the adjacent two
letters who are the same letter but case is different.
"""


class Solution:
    def makeGood(self, s: str) -> str:
        # index
        i = 0

        # loop through the input string
        while i < len(s) - 1:

            # if the two adjacent letters are the same character with different
            # cases, remove these two letters from the input string
            if s[i] != s[i + 1] and s[i].lower() == s[i + 1].lower():
                s = s[:i] + s[i + 2 :]
                if i > 0:
                    # if the index is not 0, subtract one to it because
                    # we need to recheck the previous index after removing
                    i -= 1
            else:
                i += 1

        return s
