"""
Firstly, use a list to store all the letters in the input string. Loop through the input string. If the element in the string is a letter, get the last letter in the list to the 
result. If the element is not a letter, add that element to the result.
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [l for l in S if l.isalpha()]  # only stores the letters from the string
        result = ""
        
        for l in S:
            if l.isalpha():  # loop through the string, if the current index is a letter, add the letter from the end of letters list
                result += letters.pop()
            else:
                result += l
        
        return result
