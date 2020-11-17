"""
Tried to not use any lower(), upper(), islower(), and isupper(). Created two list which stores the upper cases and lower cases. If the letter is upper case, switch it
to corresponding lower case.
"""


class Solution:
    def to_lowercase(self, str: str) -> str:
        # lists of upper and lower case alphabet
        alph_u = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        alph_l = [
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
        s = list(str)

        for i in range(0, len(s)):
            # if the letter is upper case, replace it with the lower case letter
            if s[i] in alph_u:
                s[i] = alph_l[alph_u.index(s[i])]

        return "".join(s)
