"""
This solution got rid of the nested for loop.
It adds every word's prefix (equal to the length of the searchWord) to a list
(empty string for word that is shorter than the searchWord). Then determine if
the searchWord is in the list
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # split the sentence to words
        words = sentence.split()
        # this list is used to store the prefix of the words
        modified = []

        # add every word's prefix to the list
        # word that is shorter than the searchWord will add an empty string to
        # the list
        for word in words:
            if len(word) < len(searchWord):
                modified.append("")
                continue
            modified.append(word[: len(searchWord)])

        # check if the searchWord is one of the word's prefix
        if searchWord in modified:
            return modified.index(searchWord) + 1

        return -1
