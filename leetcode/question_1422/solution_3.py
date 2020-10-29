"""
This solution is pretty similar to the solution 2 but it does not store the
left and right substring in variables. It first counts all the ones in the
input string and sees the whole input string as the right substring,
then it iterate through the input string. As its iterating through the input
string, it is adding zeros and subtracting ones simulating the left substring.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        # initialize variables to track the number of ones zeros and max score
        ones = 0
        zeros = 0
        score = 0

        # get the number of ones in the input string
        for digit in s:
            if int(digit) == 1:
                ones += 1

        # this for loop is where it separates the left and right substring
        # the index smaller than i is the left substring so we are adding 1
        # to the zeros, and the index greater than i is the right substring so
        # we are subtracting 1 from ones once the i go over.
        for i in range(len(s) - 1):
            if int(s[i]) == 0:
                zeros += 1
            else:
                ones -= 1

            # get the max score
            score = max(score, ones + zeros)

        return score
