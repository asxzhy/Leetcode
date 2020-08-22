"""
In this solutin, I simplified the solution I had previously. In this solution, I go straight to check how many difference the two strings have. If the two strings are same, 
loop through the string A and check if there is duplicated letters. If there are two differences, check if they are same after swapping the letters. If there are other amount 
of differences return false.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        
        diff = 0  # how many different letters the two strings have
        pos = []  # the index of the difference
        letters = ""  # stores all the letters that the string has
        
        for i in range(0, len(A)):
            if A[i] != B[i]:
                diff += 1
                pos.append(i)
        
        if diff == 0:
            # if the two strings are the same, check if there is duplicated letters. If so, return True
            for l in A:
                if l in letters:
                    return True
                letters += l
        elif diff == 2:
            # if there are exactly two letters different. swap the letters in A and compare to B. If they are now same, return True
            return A[:pos[0]] + A[pos[1]] + A[pos[0] + 1:pos[1]] + A[pos[0]] + A[pos[1] + 1:] == B
        else:
            return False
