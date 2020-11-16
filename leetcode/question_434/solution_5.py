"""
delete all the extra spaces and the use the count method to find how many blank
spaces there are to find out how many segments the input has
"""


class Solution:
    def count_segments(self, s: str) -> int:
        s = list(s)
        indexes = []  # used to store the extra spaces that needs to be removed
        count = 0  # used to keep track of the length of the s

        for i in range(0, len(s)):
            # if there are two spaces in a row, append in indexes and latter
            # remove the extra space
            if s[i] == " " and (i == 0 or s[i - 1] == " "):
                indexes.append(i)

        for i in indexes:
            s.pop(i + count)
            count -= 1

        if len(s) > 0 and s[-1] != " ":
            return s.count(" ") + 1

        return s.count(" ")
