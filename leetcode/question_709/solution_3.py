"""
Tried to use lower() and isupper() instead of two lists. Wanna see the difference in speed (negligible)
"""


class Solution:
    def to_lowercase(self, str: str) -> str:
        s = list(str)
        for i in range(0, len(s)):
            if s[i].isupper():
                s[i] = s[i].lower()

        return "".join(s)
