"""
This solution is pretty similar to the previous solution. It used two pointers to point to different variables. I used two while loops for the pointer to quickly go to the index 
where I want them to be. Finally, add non-letter to the result if the next index is a non-letter in S, else add the reversed letters.
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S_rev = list(S)[::-1]  # reverse the whole string
        result = ""

        i1 = 0  # index for S
        i2 = 0  # index for S_rev
        while i1 < len(S) or i2 < len(S_rev):
            while i1 < len(S) and S[i1].isalpha():
                i1 += 1  # get to the index of non-letter character
            while i2 < len(S_rev) and not S_rev[i2].isalpha():
                i2 += 1  # get to the index of letter
            
            if i1 >= len(S) and i2 >= len(S_rev):
                break  # after the two while loops, if all the index are out of range, break
            
            if len(result) == i1:  # if the next index is a non-letter in S, then add that character
                result += S[i1]
                i1 += 1
            else:  # else we add the reversed letter in the result
                result += S_rev[i2]
                i2 += 1

        return result
