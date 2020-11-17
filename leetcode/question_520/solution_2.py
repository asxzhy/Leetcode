"""
same as the previous solution
"""


class Solution:
    def detect_capital_use(self, word: str) -> bool:
        a = True
        for i in range(1, len(word)):
            if word[i].isupper():
                a = False

        return word.isupper() or word.islower() or a
