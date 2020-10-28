"""
this solution uses the the count method for String
O(n)
"""


class Solution:
    def stringMatching(self, words):
        res = []
        string = " ".join(words)

        for i in words:
            if string.count(i) > 1:
                res.append(i)

        return res
