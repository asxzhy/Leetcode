"""
loop through the string from the front and back at the same time. Search for
the same substring at the front and back. If the substring is found, check to
see if it can be multiplied to get to the exact length of the input string,
and finally check to see if the substring is same as the input string when it
is multiplied by an integer.
"""


class Solution:
    def repeated_substring_pattern(self, s: str) -> bool:
        i = 1  # left pointer
        r = len(s) - 1  # right pointer

        while i <= r:
            # check when the front and back strings are same, see if the
            # substring can be multiplied by an integer to be the length of
            # the entire s string, and then check if the strings are the same
            # when the substring is multiplied by that integer
            if (
                s[:i] == s[r:]
                and len(s) % len(s[:i]) == 0
                and s[:i] * (len(s) // len(s[:i])) == s
            ):
                return True
            i += 1
            r -= 1

        return False
