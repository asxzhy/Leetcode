"""
This solution is pretty similar to solution 3, I omitted to compare the whole strings, instead I only compared the two difference letters after swapping.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        # if the two strings are the same and have duplicate, return True
        if A == B and len(set(A)) < len(B): return True
        
        pair = []  # store the pair of different letters
        
        for i in range(0, len(A)):
            if A[i] != B[i]:
                pair.append([A[i], B[i]])
            if len(pair) > 2:  # if there are more than two pairs of different letters, return false
                return False
        
        # if there are only two pairs of different letters and they are the same after swapping, return true, otherwise false
        return len(pair) == 2 and pair[0] == pair[1][::-1]
