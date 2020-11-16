"""
Tried to do it in two for loop. First loop go over every single number in the
input string, second loop go over every two elements. Used a count to see if
the substring has the same amount of zero's and one's, then used the first
half of the substring to determine if the half of the substring only contains
zero or one. However, this method is too slow.
"""


class Solution:
    def count_binary_substrings(self, s: str) -> int:
        # store the amount of substrings that satisfy the description of the
        # problem
        count = 0

        for i in range(0, len(s)):
            for y in range(i + 2, len(s) + 1, 2):
                # if the numbers of zero and one in the string are the same,
                # check if half of the string only contains zero or one
                if s[i:y].count("0") == s[i:y].count("1") and not (
                    "0" in s[i : i + ((y - i) // 2)]
                    and "1" in s[i : i + ((y - i) // 2)]
                ):
                    count += 1

        return count
