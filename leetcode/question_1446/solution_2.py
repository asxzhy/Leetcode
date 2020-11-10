"""
This solution records the previous index where the character changes and
compute the difference between each index where changing character exists.
the longest difference will be the final result
"""


class Solution:
    def maxPower(self, s: str) -> int:
        # if the length of the input string is one, the answer is one
        if len(s) == 1:
            return 1

        maximum = 0  # the maximum length of unique characters' group
        prev = 0  # the previous index where the character changes
        i = 1  # the current index

        # iterate through the input string and get the length of every
        # unique characters' group
        while i < len(s):
            # if the character changes, compute the length of the unique
            # character group
            if s[i - 1] != s[i]:
                maximum = max(maximum, i - prev)
                prev = i

            # if the current index is the last element, get the length of the
            # last group
            if i == len(s) - 1:
                maximum = max(maximum, i - prev + 1)
            i += 1

        # if the input string has all characters the same, then the result is
        # the length of the string
        if maximum == 0:
            maximum = len(s)

        return maximum
