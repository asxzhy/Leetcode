"""
This solution split the sentence into a list of words and add the spaces in
between each word using string concatenation
"""


class Solution:
    def reorder_spaces(self, text: str) -> str:
        # count the amount of spaces
        spaces = text.count(" ")
        # get all the words
        words = text.split()
        # initialize a result string initially storing the first word
        res = words[0]

        # if there is only one word, add all the spaces to the end and return
        if len(words) == 1:
            return res + " " * spaces

        # calculate the equal amount of spaces between each word
        amount = spaces // (len(words) - 1)
        for i in range(1, len(words)):
            # add the appropriate amount of spaces and the next word
            res += " " * amount + words[i]
        # add the last word and the remaining spaces
        res += " " * (spaces - amount * (len(words) - 1))

        return res
