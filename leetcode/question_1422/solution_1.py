"""
This solution iterates through the input string and go through all the
possibilities of potential right and left substrings. Calculate the scores
and get and maximum score.
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

            # calculate the number of zeros in the left substring and
            # the number of ones in the right substring
            zeros = sum(int(zero) == 0 for zero in left_sub)
            ones = sum(int(ones) == 1 for ones in right_sub)

            # get the maximum score
            if score < zeros + ones:
                score = zeros + ones

        return score
