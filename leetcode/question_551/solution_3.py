"""
approch by using count method.
"""


class Solution:
    def check_record(self, s: str) -> bool:
        return not (s.count("A") > 1 or "LLL" in s)
