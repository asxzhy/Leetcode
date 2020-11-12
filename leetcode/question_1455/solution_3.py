"""
This solution used the same concept in solution 1 but did not use the second
for loop. This solution compared the full prefix instead of letter by letter
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # split the sentence to words
        words = sentence.split()
        # get the length of the searchWord
        length = len(searchWord)

        # check every word's prefix to see if it is same as the searchWord
        for word in words:
            if len(word) >= length and word[:length] == searchWord:
                return words.index(word) + 1

        return -1
