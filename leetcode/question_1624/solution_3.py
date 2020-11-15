"""
This solution should be faster than the previous two solutions because it does
not need to loop through the dictionary every time we proceed to the next
character. It calculates the length of the substring by using rindex() to get
the last same character's index. It also checks if there could be a longer
substring in the rest input string. If not, it exist the loop.
"""


class Solution:
    def max_length_between_equal_characters(self, s: str) -> int:
        # initially set the max length to -1
        maximum = -1

        i = 0
        while i < len(s):
            # get the length of the substring. If the substring does not exist
            # the length will be -1
            length = s.rindex(s[i]) - i - 1

            # check if the substring exists and the length of the substring
            # is greater
            if s.count(s[i]) > 1 and maximum < length:
                maximum = length

            # if the largest substring is already longer than the rest of the
            # string's length, there is no need to check them
            if maximum >= len(s) - i - 2:
                return maximum
            i += 1

        return maximum
