"""
modified the if statement. Now the if statement only takes one condition
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = 0

        while i < len(s):
            # check if the second index after is a "#". If so, treat the next two numbers as one number
            if s[i:i+3][-1] == "#":
                result += chr(96 + int(s[i:i + 2]))  # convert the integer to character using ascii
                i += 3
            else:
                result += chr(96 + int(s[i]))
                i += 1

        return result
