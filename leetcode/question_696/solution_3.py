"""
Same method but used a list to store the amount of each consecutive numbers
first, and then add them to the final result
"""


class Solution:
    def count_binary_substrings(self, s: str) -> int:
        groups = []  # number of each zero's and one's segments
        num = 1  # used to keep track the amount of the consecutive numbers
        count = 0  # final result

        for i in range(1, len(s)):
            if s[i - 1] == s[i]:  # if the number does not change
                num += 1
            else:
                # if the number changes, add the amount of consecutive numbers
                # then reset amount to one
                groups.append(num)
                num = 1

        # add the last the amount for the group of consecutive numbers
        groups.append(num)

        for i in range(1, len(groups)):  # add the smaller number to the count
            count += min(groups[i - 1], groups[i])

        return count
