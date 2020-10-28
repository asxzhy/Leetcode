"""
iterate through the words list. For each of the word, iterate through the
list again to find if it's another element's substring
O(n^2)
"""


class Solution:
    def stringMatching(self, words):
        res = []

        for i in range(0, len(words)):
            for j in range(0, len(words)):
                if words[i] in words[j] and j != i:
                    res.append(words[i])
                    break

        return res
