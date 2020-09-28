"""
I didn't know that subsequence don't have to be consecutive. I first solved the question as I was dealing with subarray
but it didn't work out.
"""

"""
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1: return len(s);

        # set the left and right pointer
        l = 0
        r = len(s)
        result = 0

        while l < len(s):
            # if the subarray is a palindrome, remove the subarray and then add one to result
            if s[l:r] == s[l:r][::-1]:
                s = s[:l] + s[r:]
                result += 1
                l = 0
                r = len(s)
            else:
                # if the subarray is not a palindrome. Keep searching
                l += 1
                r += 1
                if r > len(s):
                    r = len(s) - l
                    l = 0

            if len(s) == 0 or len(s) == 1:
                return result + len(s)
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # if the string is smaller than 2, the output is the length of the string because empty string takes 0 step
        # and a string with length one takes 1 step.
        # if the string is a palindrome, the output is one.
        # if the string is not a palindrome, we can first delete all of its a's or b's, then its a palindrome again,
        # so it take only 2 steps
        if len(s) <= 1:
            return len(s)
        elif s[::-1] == s:
            return 1
        else:
            return 2
