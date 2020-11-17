"""
uses a recursive function. Base case is when there is no whitespace in the
string. If there is whitespace, remove the first whitespace and all the method
again.
"""


class Solution:
    def reverse_words(self, s: str) -> str:
        # if there is no whitespace in the string, reverse the word and
        # return it
        if " " not in s[:]:
            return s[::-1]
        i = s.index(" ")  # find where the whitespace is at

        return s[:i][::-1] + " " + self.reverse_words(s[i + 1 :])
