"""
Loop through the input, add every digit to the result string. If the digits
left in the input is divisible by three, then add a dot to the result string
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        # initialize a string to store the result
        res = ""
        # convert the int to string
        n = str(n)

        # loop through the input
        for i in range(len(n)):
            # add the current digit to the result
            res += n[i]

            # calculate how many left digits there are in the input
            size = len(n) - i - 1

            # if the left digits can be exact divided by three, add a dot
            # to the result
            if size > 0 and size % 3 == 0:
                res += "."

        return res
