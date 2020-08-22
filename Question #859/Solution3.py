"""
Firstly, check if the two strings are exactly the same, if they are same, convert string A to a set and see if the length of the set changes. If the length becomes greater than 
string B that means there are duplicates, return True. The rest of the code is finding the different letters and try two swap them.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        # if the two strings are the same and have duplicate, return True
        if A == B and len(set(A)) < len(B): return True
        
        l = 0
        r = len(A) - 1
        while l < r and (A[l] == B[l] or A[r] == B[r]):
            # search for the different letters
            if A[l] == B[l]:
                l += 1
            if A[r] == B[r]:
                r -= 1
        
        if l < r:
            # check if the two strings become same after swap two letters in A
            return A[:l] + A[r] + A[l + 1:r] + A[l] + A[r + 1:] == B
        return False
