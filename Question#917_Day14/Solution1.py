"""
For this solution, I used a result list to store the reversed characters and convert it to a string at the end. I used two pointers in this solution, one point to the index of 
result (l), and the other one point to the string S (r). The pointer pointing to the result is used to store characters to the list, and the other pointer is used to loop through 
the string S backwards. If the l points to a non-letter in S, we add that character to the list, if the r points to a non-letter in S, we skip that and wait for the l pointer 
to go to that index. If the pointers are both pointing to a letter, add the letters to the list.
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if len(S) == 1: return S
        result = ["" for i in S]  # create a list with the same length of S

        l = 0  # index for result
        r = len(S) - 1  # index for S
        while l < len(S) and r >= -1:

            if not S[l].isalpha():  # if this index is not a letter in S, we add this sign to result
                result[l] = S[l]
                l += 1
            elif not S[r].isalpha():  # if this index is not a letter in S, we skip it
                r -= 1
            else:  # if both left and right index are pointing to a letter, add the letter to result
                result[l] = S[r]
                l += 1
                r -= 1

        return "".join(result)
