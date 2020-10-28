"""
This solution is same as previous one but used a counter instead
"""
import collections


class Solution:
    def sortString(self, s: str) -> str:
        # initialize and store the 26 letters in order
        characters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        result = ""
        # create a counter which will collect
        # and count all the letters in the input string
        chars = collections.Counter(s)

        # when the the result string haven't collect all the letter in the
        # input string, get the letters in the string according to its order
        # the letters should be collected from smallest to greatest and then
        # from greatest to smallest alternatively
        while len(result) < len(s):
            for char in characters:
                # if the letter is in the string and the total amount of this
                # letter left is greater than 0, add that letter to the result
                # string and then remove one letter from the input string
                if char in chars and chars[char] > 0:
                    result += char
                    chars[char] -= 1

            # reverse the characters
            characters = characters[::-1]

        return result
