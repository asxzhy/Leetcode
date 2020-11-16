"""
tried to do the same method by using recursion
"""


class Solution:
    def repeated_string_match(self, A: str, B: str) -> int:
        times = len(B) // len(A) + 2
        return self.match(A, B, 1, times)

    def match(self, a, b, count, times):
        if b in a * count:
            return count
        if count >= times:
            return -1
        count += 1

        return self.match(a, b, count, times)
