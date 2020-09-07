"""
I learnt that min() can also get the smallest character in a string. By using min() and count(), I can get the frequency of the smallest character easily. Then, just find the 
index where the number in queries becomes smaller and the rest number in words will all be greater because the list is sorted
"""

class Solution:
    def numSmallerByFrequency(self, queries, words):
        lengths = sorted(w.count(min(w)) for w in words)  # get all the length in words
        result = []
        
        for q in queries:
            q = q.count(min(q))  # length of the query
            for i in range(0, len(lengths)):
                if q < lengths[i]:  # find the first length that the query is samller than, the rest will be all smaller than it.
                    result.append(len(lengths) - i)
                    break
                if i == len(lengths) - 1:
                    result.append(0)
            
        
        return result
