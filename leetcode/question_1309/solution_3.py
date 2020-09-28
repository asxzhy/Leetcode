"""
same idea but now the while loop is iterating from the end to the beginning. This makes checking "#" sign more obvious
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = len(s) - 1

        while i > -1:
            # check if the current index is a "#". If so, the two number in front will count as a single number.
            if s[i] == "#":
                result = chr(96 + int(s[i-2:i])) + result
                i -= 3
            else:
                result = chr(96 + int(s[i])) + result
                i -= 1

        return result
