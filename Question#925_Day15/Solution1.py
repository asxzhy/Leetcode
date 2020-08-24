"""
I used two index pointers to keep track of the two strings together. This solution loop through the two strings. It checks if every letter in the two strings are the same. 
For the long pressed issue, the index for the typed string loop through all the same repeated letters when the next letter in name changes. In other words, I ignored all the 
repeated letters in the variable typed, and only checked if the other words in both strings are the same.
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name): return False  # it is not possible that typed is shorter than name
        
        i1 = 0  # index for name
        i2 = 0  # index for typed
        while i1 < len(name) and i2 < len(typed):
            if name[i1] != typed[i2]:  # if the letters in name and typed doesn't match, return false
                return False
            
            if i1 < len(name) - 1 and name[i1] != name[i1 + 1]:
                # if the letter in name changes, move the index for typed to the last same letter
                # in other words, this skips all the letters that are being long pressed
                while i2 < len(typed) - 1 and typed[i2] == typed[i2 + 1]:
                    i2 += 1
            elif i1 == len(name) - 1:
                # if it is the last letter in name, check if the typed has the same letters at the end
                return typed[i2:].count(name[i1]) == len(typed[i2:])
            
            i1 += 1
            i2 += 1
            
            # check if one of the string run out of length before the other one does
            if (i1 < len(name) and i2 >= len(typed)) or (i1 >= len(name) and i2 < len(typed)):
                return False
        
        return True
