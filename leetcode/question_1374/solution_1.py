"""
Only use letter a and b to solve this question. If the input number is odd,
return a string only consists of a's.If the input number is even, return a
string consists of one a and rest b's
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return "a" * n
        else:
            return "a" + "b" * (n - 1)
