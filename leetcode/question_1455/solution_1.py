"""
This solution compares every word's prefix to the searchWord, if the searchWord
is found them return the index + 1 if the word
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # split the sentence to words
        words = sentence.split()

        # iterate through all the words
        for word in words:
            # iterate through the letters in the searchWord
            # check if the searchWord is a prefix
            for i in range(len(searchWord)):
                if i == len(word) or searchWord[i] != word[i]:
                    break
            else:
                # if all the letters match, return the index
                return words.index(word) + 1

        # there is no word with searchWord as prefix
        return -1
