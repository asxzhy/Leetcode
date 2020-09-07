"""
Fistly, I convert the input string to a list, and then used a two pointer method to loop through the list from the beginning and end at the same time. Skip all the non-letter 
elements. If both pointer are pointing to a letter, swap them. Convert the list back to a string at the end
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if len(S) == 0: return ""
        if len(S) == 1: return S
        
        S = list(S)  # convert to list

        l = 0  # left pointer
        r = len(S) - 1  # right pointer
        while l < r:
            # if the left or right pointer is pointing to a non-letter character, move to the next index
            if not S[l].isalpha():
                l += 1
            if not S[r].isalpha():
                r -= 1
            
            # if both indexes are pointing to a letter, switch the two letters
            if S[l].isalpha() and S[r].isalpha():
                S[l], S[r] = S[r], S[l]
                l += 1
                r -= 1
        
        return "".join(S)
