"""
In this solution, I checked if the text has the same or more amount of characters that is in the word balloon. If there is, delete that character. After a round, add the result 
by one. When there is no more character can be deleted, return the result.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = "balloon"
        result = 0

        while len(text) >= len(b):
            for l in "balon":
                if b.count(l) <= text.count(l):  # if there are letters in balloon, delete the letters
                    text = text.replace(l, "", b.count(l))
                else:  # if we cannot find the balloon letter in text, return the result
                    return result
            result += 1  # after each full cycle, add one to result

        return result
