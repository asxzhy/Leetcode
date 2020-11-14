"""
This solution is similar to the first solution. It loops when the integer still
have more than three digits left. Then it adds the three digits to the result
string with a dot before them
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        # initialize a variable to store the result
        res = ""

        # loop through the input integer until it contains less than four
        # digits
        while n > 999:
            # add three digits to the result string one by one to avoid
            # special cases with 0 (e.g 001 will only add 1 to the result)
            for i in range(3):
                res = str(n % 10) + res
                n = n // 10

            res = "." + res

        # add the left digits
        res = str(n) + res
        return res
