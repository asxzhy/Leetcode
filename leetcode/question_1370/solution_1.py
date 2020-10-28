"""
The way that this code works is that first sort the string alphabetically
and convert the string to a list. Each element contains a group of same
characters. Add the characters from index 0 to len(list) and from len(list)
to 0 again.
"""


class Solution:
    def sortString(self, s: str) -> str:
        s = "".join(sorted(s))  # sort the string
        size = len(s)
        result = ""

        # find the places where the character changes
        # and add a space in between
        i = 1
        while i < len(s):
            if s[i - 1] != s[i]:
                s = s[:i] + " " + s[i:]
                i += 2
            else:
                i += 1

        # split the string based on the space we add before
        s = s.split(" ")

        # when there is still characters in the list,
        # add the characters from smallest to greatest and then
        # from greatest to smallest to the result
        while size > 0:
            for i in range(len(s)):
                if s[i]:
                    result += s[i][0]
                    s[i] = s[i][:-1]
                    size -= 1

            for i in range(len(s) - 1, -1, -1):
                if s[i]:
                    result += s[i][0]
                    s[i] = s[i][:-1]
                    size -= 1

        return result
