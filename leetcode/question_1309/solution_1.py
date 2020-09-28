"""
Iterate over the string. Convert each integer to the corresponding character using the ascii chart
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = 0

        while i < len(s):
            # check if the second index after is a "#". If so, treat the next two numbers as one number
            if len(s) - i > 2 and s[i + 2] == "#":
                result += chr(96 + int(s[i:i + 2]))  # convert the integer to character using ascii
                i += 3
            else:
                result += chr(96 + int(s[i]))
                i += 1

        return result
