"""
Change list to set because I used an if statement to check if a transformation string is in the transformations list. Then I tried to convert the conversion of the word
into a one line code, thought that might be faster. Turns out the run time doesn't improve
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()  # used to store different transformations
        trans = ""  # used to store the current word's transformation
        
        for i in range(0, len(words)):
            # for every word, get their morse code
            trans = "".join([codes[ord(letter) - 97] for letter in words[i]])
                
            # check if the morse code is same as other corse code's transformation
            if not trans in transformations:
                transformations.add(trans)
            trans = ""  # reset to empty for next word
        
        return len(transformations)
