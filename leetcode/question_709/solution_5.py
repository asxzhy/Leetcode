"""
Reviewed other people's code from discussion section. Learnt the function of
ord and chr. Tried to use them instead of the two list in solution two.
"""


class Solution:
    def to_lowercase(self, str: str) -> str:
        result = ""
        for i in range(0, len(str)):
            if ord("A") <= ord(str[i]) <= ord("Z"):
                result += chr(ord(str[i]) + 32)
            else:
                result += str[i]

        return result
