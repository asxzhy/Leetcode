"""
Same method as solution one but we starts from A is alreay longer to equal to the length of B
"""


class Solution:
    def repeated_string_match(self, A: str, B: str) -> int:
        # get the number of times we need to multiply A to get A to the same l
        # ength or longer than B
        times = -(-len(B) // len(A))

        # check if B is in A if A is repeated two more times
        for i in range(2):
            if B in A * (times + i):
                return times + i

        return -1
