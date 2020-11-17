"""
same thought process as solution two but uses for loop instead
"""


class Solution:
    def reverse_str(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i : i + k] = s[i : i + k][::-1]

        return "".join(s)
