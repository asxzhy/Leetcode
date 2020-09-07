"""
For this question we need to know if there is the same amount of same letters at even indexes and odd indexes. If the amount of same letters are the same, then they will be the 
special-equivalent strings.
Sort the even index letters and odd index letters separately. Add them together and add the whole string to a set. The set will help us to get rid of the duplicated strings. What 
left are the different special equivalent groups.
"""

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        result = set()  # used to store the wrods
        word = ""
        
        for w in A:
            # for each word, sort its even and odd indexes' characters and then add the new word to the set
            word = "".join(sorted(w[0::2])) + "".join(sorted(w[1::2]))
            result.add(word)
        
        return len(result)
