"""
This solution kind of similar to solution one but it does not need to iterate
through the dictionary whenever the index changes. It stores the length's
information in the dictionary and get the longest length by using max().
"""


class Solution:
    def max_length_between_equal_characters(self, s: str) -> int:
        # create a dictionary.
        # It has the format of {character : [first_index, length_of_substring]}
        lengths = {}

        for i in range(len(s)):
            char = s[i]

            # if the current character exists in the dictionary, calculate the
            # length of the substring and store it
            if char in lengths:
                lengths[char][1] = i - lengths[char][0] - 1
            else:
                # if the character is not in the dictionary, add it to the
                # dictionary with a initial value of [index, -1]
                lengths[char] = [i, -1]

        # if there is no substring, return -1. Else return the largest length
        # in the dictionary
        if not lengths:
            return -1
        return max(length[1] for length in lengths.values())
