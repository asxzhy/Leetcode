"""
same concept but used for each loop, this one is a little faster than the first
solution
O(n^2)
"""


class Solution:
    def stringMatching(self, words):
        res = []

        for i in words:
            for j in words:
                if i in j and i is not j:
                    res.append(i)
                    break

        return res
