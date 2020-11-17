"""
By using two while loop to accomplish the problem, the outer while loop is used
to loop through the string, the inner while loop is used to count for the 2k
characters when we find all the 2k characters, we reverse the second half of
the 2k characters.
"""


class Solution:
    def reverse_str(self, s: str, k: int) -> str:
        # if the length of the input string is less than the integer k, reverse
        # the input string
        if len(s) < k:
            re = s[::-1]
        else:
            # else just reverse the first k characters
            re = s[k - 1 :: -1]
        i = k
        length = 0

        # the loop starts after the kth character
        while i < len(s):
            # check if there is enough characters
            while length < 2 * k and i < len(s):
                # add the first k characters in the re string
                if length < k:
                    re += s[i]
                length += 1
                i += 1

            # if there is not enough characters, add the reversed characters
            # after the first k characters
            if length < 2 * k:
                re += s[i - length + k :][::-1]
            else:
                # if there is enough character, add teh reversed characters.
                re += s[i - k : i][::-1]
            length = 0

        return re
