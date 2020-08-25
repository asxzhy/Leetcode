"""
I learnt that bisect.bisect alows me to find where the number can be inserted so that the list remains sorted.
"""

class Solution:
    def numSmallerByFrequency(self, queries, words):
        lengths = sorted(w.count(min(w)) for w in words)  # get all the length in words
        result = []
        
        for q in queries:
            q = q.count(min(q))  # length of the query
            result.append(len(lengths) - bisect.bisect(lengths, q))
            
        return result
