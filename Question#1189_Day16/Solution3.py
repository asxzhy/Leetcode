"""
In this solution, we create a dictionary full of letters from balloon manually. Then, add the same characters in text to the dictionary in order to know its frequency in the text.
Then, we divide the l, and o by two and get the minimum frequency out of the five characters.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {"b":0, "a":0, "l":0, "o":0, "n":0}  # create a dictionary with characters in balloon
        for char in text:  # only add the characters in balloon to the dictionary
            if char in counter:
                counter[char] += 1
        
        counter["l"] //= 2  # divide "l" and "o" by two because there are two l's and o's in balloon
        counter["o"] //= 2
        
        return min(counter.values())  # get the smallest number of character.
