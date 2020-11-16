"""
Tried to do it in recursion but it is very slow compare to solution one and
two. Thought from leetcode discussion
"""


class Solution:
    def valid_palindrome(self, s: str) -> bool:
        return self.is_palindrome(0, len(s) - 1, s, True)

    def is_palindrome(self, i, r, s, skip):
        # stop when l is greater or equal to r
        if i >= r:
            return True

        # if left character is equal to right character, go to the next
        # characters
        if s[i] == s[r]:
            return True and self.is_palindrome(i + 1, r - 1, s, skip)
        elif not skip:
            # if the characters are not the same, and we have already skipped
            # a character, return false
            return False
        else:
            # if te characters are not the same, but we haven't skipped a
            # character, try to skip the left character or the right character
            return self.is_palindrome(i + 1, r, s, False) or self.is_palindrome(
                i,
                r - 1,
                s,
                False,
            )
