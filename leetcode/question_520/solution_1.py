"""
There are three possibilities. One is all lower cases, second one is first letter is upper case and the rests are lower cases, and the last one is all upper cases.
Therefore, we could check if the first letter's case. If the first letter is upper case, check for case changes after the second letter. If the first letter is lower cases,
all the rests have to be lower cases.
"""


class Solution:
    def detect_capital_use(self, word: str) -> bool:
        for i in range(1, len(word)):
            if word[0].isupper():

                # check if the case changes after the first letter
                if word[1].isupper() != word[i].isupper():
                    return False
            else:
                # check if the case is upper if the first letter is upper case
                if word[i].isupper():
                    return False

        return True
