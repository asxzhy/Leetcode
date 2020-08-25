"""
I firstly separeted the sentence to a list of words. Then for every word, I checked if the first letter is a vowel. If it's a vowel, then do the correspongind conversion for the 
word. If it is not a vowel, do the other conversion. Join the list back together and return the sentence
"""

class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split()  # seperate the words
        
        for i in range(0, len(S)):
            if S[i][0] in "aeiouAEIOU":  # if the word starts with a vowel, add ma to the end and then add some amount of a
                S[i] = S[i] + "ma" + "a" * (i + 1)
            else:  # if the word starts with consonant, add the first letter to the end and then add ma
                S[i] = S[i][1:] + S[i][0] + "ma" + "a" * (i + 1)
        
        return " ".join(S)
