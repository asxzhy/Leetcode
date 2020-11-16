"""
By using split() method, we can split one sentence down and get the number
of segments.
"""


class Solution:
    def count_segments(self, s: str) -> int:
        return len(s.split())
