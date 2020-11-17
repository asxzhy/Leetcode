"""
First check if the input string is already a palindrome. Check if the character
starts from the left and right of the list are the same one by one.
If the characters are not the same, try to delete one of the character and
then compare to see if the string is palindrome. If the string is still not a
palindrome then return false
"""


class Solution:
    def valid_palindrome(self, s: str) -> bool:
        # check if it's a palindrome
        if s[: len(s) // 2][::-1] == s[len(s) // 2 + len(s) % 2 :]:
            return True

        s = list(s)  # convert the string to a list
        temp = s[:]  # make a copy of the list
        i = 0  # left pointer
        r = len(s) - 1  # right pointer
        while i < r:
            # if the two letters are not same
            if s[i] != s[r]:
                # try to delete one of them and then compare if the string
                # is a palindrome
                del temp[i]
                if (
                    temp[: len(temp) // 2][::-1]
                    == temp[len(temp) // 2 + len(temp) % 2 :]
                ):
                    return True

                # try to delete the other one
                temp = s[:]
                del temp[r]
                if (
                    temp[: len(temp) // 2][::-1]
                    == temp[len(temp) // 2 + len(temp) % 2 :]
                ):
                    return True

                # if the string is still not the same, return false
                return False
            i += 1
            r -= 1
