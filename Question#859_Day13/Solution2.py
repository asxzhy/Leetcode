"""
I used a set to check if there is duplicated letters. In this method I used a two pointer to find the two different letters. If the left pointer becomes greater than the right 
pointer, that means the two strings are same and I need to check if there is duplicate in the string in order to determine whether to output true or false. If there are 
exactly two different letters, check if the two strings are the same after swapping the two letters.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False  # if the length of the two strings are not the same return false
        letters = set()  # used to store the different letters
        is_greater = False  # if there is one letter's frequency is greater than 1, this boolean becomes True. This variable is only going to be used when the two strings are the same
        
        l = 0
        r = len(A) - 1
        while l < r and (A[l] == B[l] or A[r] == B[r]):
            if not is_greater and l < r:  # if did not find any letter with frequency greater than one, keep track of the letters' frequency
                if A[l] not in letters:
                    letters.add(A[l])
                else:
                    is_greater = True
                if A[r] not in letters:
                    letters.add(A[r])
                else:
                    is_greater = True
            
            if A[l] == B[l]:
                l += 1
            if A[r] == B[r]:
                r -= 1
            
        if l < r:  # if the two strings are not the same, check if they are the same when 
            return A[:l] + A[r] + A[l + 1:r] + A[l] + A[r + 1:] == B
        elif l == len(A) - r - 1:
            return is_greater
        else:
            return False
