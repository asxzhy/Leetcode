"""
First check if both A and B strings are empty or if A is empty.
Return the result. Find how many times A has to repeated it self to be the same
length as B or a little longer than B and then add two to that number. We add
two because A might be something like "abc" and B might be "cabca", which means
we need to repeat A two more times to make sure we have covered all the
possibilities.
"""


class Solution:
    def repeated_string_match(self, A: str, B: str) -> int:
        # if both strings are empty, return 1
        if len(A) == len(B) == 0:
            return 1
        # if A is empty, return -1
        if len(A) == 0:
            return -1

        times = len(B) // len(A) + 2  # check how many longer is B compare to A
        A_temp = A  # used to store repeated string A

        # used to check if B is a substring of repeated A
        for i in range(1, times + 1):
            if B in A_temp:
                return i
            A_temp += A

        return -1
