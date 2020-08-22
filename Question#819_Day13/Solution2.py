"""
For this solution, I used a dictionary to store each word and its frequency. At the beginning, I looped through the paragraph and replaced all the unnecessary puncatuations.
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        words = {}  # used to store all the words and its total amount
        maximum = 0  # store the maximum times of a word occurred
        result = ""
        
        for l in paragraph:
            # remove all the unnecessary punctuactions
            if not l.isalpha():
                paragraph = paragraph.replace(l, " ")
        paragraph = paragraph.lower().split()
        
        for word in paragraph:
            if word in banned:  # if the word is banned, continue to the next cycle
                continue
            elif word in words:  # if the word isn't a new word, add its frequency by one
                words[word] += 1
            else:  # if it's a new word, add the word to the dictionary
                words[word] = 1
            
            if words[word] > maximum:  # keep track of the most frequent word in the dictionary
                maximum = words[word]
                result = word
        
        return result
