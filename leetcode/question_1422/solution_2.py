"""
This solution is same as the solution one but improved some methods.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        # create variables for the left half and right half substring of the
        # input string
        left_sub = ""
        right_sub = ""

        score = 0
        # iterate through the input string to go over all the possibilities
        for i in range(1, len(s)):
            # get the left and right substring of the input string
            left_sub = s[:i]
            right_sub = s[i:]

            # use the count method instead of looping through the left and
            # right substring
            zeros = left_sub.count("0")
            ones = right_sub.count("1")

            # use a max method instead of a if statement
            score = max(score, zeros + ones)

        return score
