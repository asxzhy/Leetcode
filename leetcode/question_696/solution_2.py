"""
Look for the place where the number changes. Keep track of the previous and
current amount of consecutive numbers and add the fewer number to the variable
count, when encounter the next change of numbers. We add the fewer number
because the number of substring that has the same amount of zero's and one's
depend on the fewer number. E.g: "00011". There are three zero's and two
one's. We have "0011", and "01" substring that satisfy the problem.
"""


class Solution:
    def count_binary_substrings(self, s: str) -> int:
        prev = 0  # store the total amount of the preivous number
        cur = 1  # store the total amount of the current number
        count = 0  # store the total amount of substrings

        for i in range(1, len(s)):
            # if the number changes from zero to one or one to zero
            if s[i - 1] != s[i]:
                # add the number of fewer number occurred
                count += min(prev, cur)
                prev = cur
                cur = 1
            else:
                cur += 1

        return count + min(prev, cur)
