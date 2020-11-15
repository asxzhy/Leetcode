"""
This solution is similar to the solution one but used a int max to store the
greatest length instead of a list. Therefore this solution takes up lesser
memory
"""


class Solution:
    def max_length_between_equal_characters(self, s: str) -> int:
        # create a dictionary, and a max to store the greatest length
        dic = {}
        maximum = -1

        for char in s:
            # increase all the values in the dictionary by one
            for key in dic.keys():
                dic[key] += 1

            # if the current character is in the dictionary, that means we
            # encountered the second character. Check if this substring is
            # greater, if so, change max to it.
            if char in dic and maximum < dic[char] - 1:
                maximum = dic[char] - 1

            # else if the character is not in the dictionary, add it to the
            # dictionary with a value of zero
            if char not in dic:
                dic[char] = 0

        return maximum
