"""
turn the string into a list. This list only contains words from the input
string. Reverse all the words in the list, and then merge the list back
together with a
"""


class Solution:
    def reverse_words(self, s: str) -> str:
        s = s.split()  # split the string by a whitespace into a list

        # reverse every word in the list
        for i in range(0, len(s)):
            s[i] = s[i][::-1]

        # merge the list together with a whitespace in between
        return " ".join(s)
