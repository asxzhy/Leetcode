"""
I kept the set but got rid of the one line code which converts the word into morse code. Run time decreases.
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()  # used to store different transformations
        trans = ""  # used to store the current word's transformation
        
        for i in range(0, len(words)):
            # for every word, get their morse code
            for letter in words[i]:
                trans += codes[ord(letter) - 97]
                
            # check if the morse code is same as other corse code's transformation
            if not trans in transformations:
                transformations.add(trans)
            trans = ""  # reset to empty for next word
        
        return len(transformations)
