"""
This solution uses the same concept to solve the solution but it used the
enumerate for loop.
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # split the sentence to words
        words = sentence.split()
        # get the length of the searchWord
        length = len(searchWord)

        # check every word's prefix to see if it is same as the searchWord
        for i, word in enumerate(words, 1):
            if searchWord in word and word[:length] == searchWord:
                return i

        return -1
