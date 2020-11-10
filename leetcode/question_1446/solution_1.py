"""
This solution split the string into groups of unique characters. Then find the
greatest length among the groups
"""


class Solution:
    def maxPower(self, s: str) -> int:
        i = 1
        # iterate through the string and add whitespaces between characters
        # that are not the same
        while i < len(s):
            if s[i - 1] != s[i]:
                s = s[:i] + " " + s[i:]
                i += 1
            i += 1

        # split the string into a list
        s = s.split(" ")

        # find the maximum length among the groups of unique characters
        maximum = 0
        for i in s:
            if maximum < len(i):
                maximum = len(i)

        return maximum
