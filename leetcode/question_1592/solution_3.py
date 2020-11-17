"""
This solution is similar to solution 1 but used fstring and modified the
for loop
"""


class Solution:
    def reorder_spaces(self, text: str) -> str:
        # get the total amount of spaces
        spaces = text.count(" ")
        # get all the words in a list
        words = text.split()
        # initialize a result variables
        res = ""

        # if there is only one word, add all the spaces to the end and return
        if len(words) == 1:
            return f'{words[0]}{" " * spaces}'

        # calculate the amount of spaces needed to be placed between words
        # and the leftover spaces
        equal_space = spaces // (len(words) - 1)
        extra_space = spaces % (len(words) - 1)

        # loop through the words, and add all the spaces between each word
        for i in range(len(words)):
            res += words[i]
            if i < len(words) - 1:
                res = f'{res}{" " * equal_space}'
            else:
                res = f'{res}{" " * extra_space}'

        return res
