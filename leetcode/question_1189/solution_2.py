"""
I learnt the counter method in collectins. This counter converts a string to a dictionary with every character as a single key and the character's frequency as its value. 
Also, counter allows calling something that it does contain, and it will return a zero. This solution converts the text and balloon to counter and then divide the frequency 
of each character in balloon to get how many balloon is in the text.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)  # this will store all the letters in text and the letter's amount
        balloon = collections.Counter("balloon")
        
        # find out the smallest num
        return min([count[num] // balloon[num] for num in balloon])
