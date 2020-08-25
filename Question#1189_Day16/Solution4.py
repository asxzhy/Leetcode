"""
This solution uses the characteristic of Counter to get the frequency of each character in balloon. If there is a character does not exist in the counter, the counter will 
return zero. 
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)
        
        # this can work because Counter returns zero if it cannot find the key
        return min(count["b"], count["a"], count["l"]//2, count["o"]//2, count["n"])
