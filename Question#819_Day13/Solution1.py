"""
I used two lists to store the basic information from the paragraph. One list stores every word that occurs in the paragraph (does not contain duplicates). The other list stores 
the frequency of each word's usage. I used another string to keep track of each word when I loop through the paragraph letter by letter. If the word is not already in the 
list and it is not banned, the word will be added to the list and it's frequency will be recorded. I get the most frequency at the end and output the cooresponding word. 
At the first, I was going to use a 2D list to store the word and its frequency together. -> [["bob", 1], ["hits", 1], ["ball", 2]]
However, I thought that I need an additional loop for finding the maximum frequency, so I changed to to lists instead. There is another solution which used a dictionary to 
solve this problem.
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        paragraph += " "  # add an additional whitespace to the end of the paragraph
        words = []  # used to store all the words
        counts = []  # number of times the words occurs in the paragraph
        word = ""

        for i in range(0, len(paragraph)):
            if (paragraph[i] == " " or not paragraph[i].isalpha()) and word != "":
                if word not in words and word not in banned:  # if it's a new word and isn't banned
                    words.append(word)
                    counts.append(1)
                elif word not in banned:
                    counts[words.index(word)] += 1
                word = ""
            elif paragraph[i].isalpha():  # get the word from the sentence and change it to lower case
                word += paragraph[i].lower()

        if len(words) == 1:
            return words[0]
        else:
            return words[counts.index(max(counts))]  # get the word which occurs most in the paragraph
