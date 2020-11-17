"""
This solution uses a dictionary to track all of the substring's length and
if the substring exists (the second same character exists), calculate the
length and add the length to the lengths list. Finally get the greatest
number in the length
"""


class Solution:
    def max_length_between_equal_characters(self, s: str) -> int:
        # create a dictionary and list
        dic = {}
        lengths = []

        for char in s:
            # increase add all the values in the dictionary by one
            for key in dic.keys():
                dic[key] += 1

            # if the current character is in the dictionary, that means we
            # encountered the second character and add the length of that
            # substring to the lengths list
            if char in dic:
                lengths.append(dic[char] - 1)

            # else if the character is not in the dictionary, add it to the
            # dictionary with a value of zero
            if char not in dic:
                dic[char] = 0

        # if there is no substrings, which means there are no same characters
        # in the input string. Return -1, else return the greatest lengths
        if lengths:
            return max(lengths)
        else:
            return -1
