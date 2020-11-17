"""
Tried to use a string to store the result instead of convert the input string
to a list. Wanna see the difference (still negligible)
"""


class Solution:
    def to_lowercase(self, str: str) -> str:
        result = ""
        for i in range(0, len(str)):
            if str[i].isupper():
                result += str[i].lower()
            else:
                result += str[i]

        return result
