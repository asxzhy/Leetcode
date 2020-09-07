"""
In this solution, I used one variable to keep track of the name string. For the typed string, I used a for loop to loop through it. The for loop skips the letters in the variable 
typed when the previous letter is same as the current letter in typed. Other function similar to the solution 1. At the end, I checked if i is the length of name to ensure we 
have gone over all the letters in name.
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0  # index for name
        for j in range(0, len(typed)):
            if i < len(name) and typed[j] == name[i]:  # if the letter in name and typed is same, go to the next index
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                # if the letter is not the same at the first index or if the previous letter in typed does not repeat, return false
                return False
        
        return i == len(name)  # this makes sure we go over all the letters in name
