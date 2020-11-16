"""
loop through the input, each time the length of substring gets smaller by one
"""


class Solution:
    def find_LUS_length(self, a: str, b: str) -> int:
        # find out which input is longer and which one is shorter
        if len(a) <= len(b):
            short = a
            long = b
        else:
            short = b
            long = a

        i = 0  # left pointer
        r = len(long)  # right pointer

        # loop through the input, each time the length of substring gets
        # smaller by one
        while i < r:
            # check every possibility with that length of substring
            while r <= len(long):

                # if the substring is uncommon, return the length
                if short.find(long[i:r]) == -1:
                    return len(long[i:r])

                i += 1
                r += 1

            r = len(long) - i
            i = 0

        return -1
