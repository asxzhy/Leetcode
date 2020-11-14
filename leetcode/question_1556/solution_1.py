"""
Loop through every three digits in the input integer from back to front.
Add a dot before the three digits.
If there is only three or less digit left, add all the digits to the result
string without the dot
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        # initialize a string to store the result string
        res = ""
        # converts the integer to a string
        n = str(n)

        # loop through the input string from back to front until the index is
        # less or equal to 3 (there is 3 or less than 3 digits left)
        i = len(n)
        while i > 3:
            # add the dot and three digits in the input to the front of the
            # result string
            res = "." + n[i - 3 : i] + res
            i -= 3

        # add the left digits if there are any and return the result
        res = n[:i] + res
        return res
