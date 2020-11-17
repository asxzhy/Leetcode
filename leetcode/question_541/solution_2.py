"""
using recursive, devide the question into various 2k characters problems
"""


class Solution:
    def reverse_str(self, s: str, k: int) -> str:
        if not s:
            return ""

        return s[:k][::-1] + s[k : 2 * k] + self.reverseStr(s[2 * k :], k)
