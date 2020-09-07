"""
Learnt that set does not allow duplicate elements in it. So I got rid of the if statement.
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()  # used to store different transformations
        
        for i in range(0, len(words)):
            trans = ""  # used to store the current word's transformation
            # for every word, get their morse code
            for letter in words[i]:
                trans += codes[ord(letter) - 97]
                
            transformations.add(trans)
        
        return len(transformations)
