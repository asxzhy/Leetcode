"""
Same method but avoid some addition
"""


class Solution:
    def repeated_string_match(self, A: str, B: str) -> int:
        # get the number of times we need to multiply A to get A to the same
        # length or longer than B
        times = -(-len(B) // len(A))

        # check if B is in A if A is repeated two more times
        for i in range(times, times + 2):
            if B in A * i:
                return i

        return -1
