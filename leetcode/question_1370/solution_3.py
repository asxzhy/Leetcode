"""
This solution iterates a list contains the 26 characters back and forth to get
the characters in the given string according to their order. This solution
should have a smaller time complexity compared to the previous solution
"""


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

        # when the input string is not empty,
        # get the letters in the string according to its order
        # the letters should be collected from smallest to greatest
        # and then from greatest to smallest alternatively
        while len(s) > 0:
            for char in characters:
                # if the letter exist in the input string,
                # add the letter to the result, and then remove this letter
                # in the input string
                if char in s:
                    result += char
                    i = s.index(char)
                    s = s[:i] + s[i + 1 :]

            # reverse the characters
            characters = characters[::-1]

        return result
