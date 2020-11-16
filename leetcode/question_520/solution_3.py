"""
When the letters after the first letter are all lower case, it doesn't matter
what case is for the first letter. We need to add a possibility for only one
letter in the input string since we are not checking the first letter when the
word is not all capital
"""


class Solution:
    def detect_capital_use(self, word: str) -> bool:

        return word.isupper() or word[1:].islower() or len(word) < 2
