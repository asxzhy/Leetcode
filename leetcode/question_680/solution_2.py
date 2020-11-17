"""
Same thought process but gets rid of the characters that have been checked.
Only compare the characters that are left (ignore the characters that have been
checked to be same).
"""


class Solution:
    def valid_palindrome(self, s: str) -> bool:
        i = 0

        while i < len(s) // 2 and s[i] == s[-(i + 1)]:
            i += 1

        s = s[i : len(s) - i]

        return s[1:][::-1] == s[1:] or s[:-1][::-1] == s[:-1]
