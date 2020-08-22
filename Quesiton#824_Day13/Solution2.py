"""
This is same as the last solution but I tried to use set to see if the program can be any fast. It turns out to be the same
"""

class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split()  # seperate the words
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        
        for i in range(0, len(S)):
            if S[i][0] in vowels:  # if the word starts with a vowel, add ma to the end and then add some amount of a
                S[i] = S[i] + "ma" + "a" * (i + 1)
            else:  # if the word starts with consonant, add the first letter to the end and then add ma
                S[i] = S[i][1:] + S[i][0] + "ma" + "a" * (i + 1)
        
        return " ".join(S)
