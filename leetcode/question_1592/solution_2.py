"""
This solution is similar to solution 1 but uses a list instead of string to
get the result.
"""


class Solution:
    def reorder_spaces(self, text: str) -> str:
        # get the total amount of spaces in the input string
        spaces = text.count(" ")
        # get all the words in a list
        words = text.split()
        # get the amount of words minus 1
        count = len(words) - 1

        # if there is only one word, add all the spaces to the end and return
        if len(words) == 1:
            return words[0] + " " * spaces

        # calculate the equal amount of spaces between each word
        amount = spaces // (len(words) - 1)

        # loop through the list and insert the spaces between each word
        i = 1
        while i < len(words):
            words.insert(i, " " * amount)
            i += 2

        # add the remaining spaces, turn the list into a string and return
        res = "".join(words) + " " * (spaces - amount * count)

        return res
