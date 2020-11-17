"""
Same method but used for loop instead of recursive.
"""


class Solution:
    def check_record(self, s: str) -> bool:
        countA = 0  # used to count the amount of "A"
        countL = 0  # used to count the amount of continuous "L"

        for i in s:
            if i == "A":
                countA += 1
            if i == "L":
                countL += 1

            # if the letter is not "L", reset countL to 0 becasue the "L" has
            # to be continuous
            if i != "L":
                countL = 0

            # conditions that we need to return False
            if countA > 1:
                return False
            if countL > 2:
                return False

        return True
