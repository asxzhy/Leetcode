"""
This solution loop through the input string and add the letters one by one to
the result list. If the letter in the input string is same as the last letter
in the list and their cases are different, then remove the last letter in the
list.
This solution is similar to solution 1 but does not need to go back one index
whenever we remove a pair of letters
"""


class Solution:
    def makeGood(self, s: str) -> str:
        # initialize a list to store the letters
        res = []

        for letter in s:
            # if the list is not empty and the letter at the current index is
            # the same character with different case as the last letter in the
            # list (which means they are adjacent), remove the letter from the
            # list
            if len(res) > 0 and res[-1] != letter and res[-1].lower() == letter.lower():
                res.pop()
            else:
                res.append(letter)

        return "".join(res)
