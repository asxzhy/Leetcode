"""
Use a list to store all the different transformations. Only new transformations can be added to the list. For every word in the input list, turn them into morse code
by using the provided morse code list. Return the transformations list's length at the end.
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = []  # used to store different transformations
        trans = ""  # used to store the current word's transformation
        
        for i in range(0, len(words)):
            # for every word, get their morse code
            for letter in words[i]:
                trans += codes[ord(letter) - 97]
                
            # check if the morse code is same as other corse code's transformation
            if not trans in transformations:
                transformations.append(trans)
            trans = ""  # reset to empty for next word
        
        return len(transformations)
